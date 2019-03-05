package com.codingame.game;

import java.util.*;
import java.lang.Math;

import com.codingame.gameengine.core.AbstractPlayer.TimeoutException;
import com.codingame.gameengine.core.AbstractReferee;
import com.codingame.gameengine.core.GameManager;
import com.codingame.gameengine.core.SoloGameManager;
import com.codingame.gameengine.module.entities.*;
import com.google.inject.Inject;
import com.google.inject.Provider;

public class Referee extends AbstractReferee {
    @Inject private SoloGameManager<Player> gameManager;
    @Inject private GraphicEntityModule graphicEntityModule;

    private int exp_max=6; // pour prévoir la dimensions des arrays dans l'IA

    private int rows,columns; // !! Val max pour rows : 2**exp_max-1
    private int[][] x;

    private Rectangle[][] grille_graphique;
    private Circle[][] jetons_graphique;
    private int dim_cases;
    private int origines_x;
    private int origines_y;
    private int[] couleurs={0xf2b213,0x22a1e4};
    private Action lastAction = null;
    private Player player;
    private String[] noms;
    private String[] avatars;

    private boolean premiere_annonce=true;



    @Override
    public void init() {
        // On récupère les entrées du test
        List<String> inputs = gameManager.getTestCaseInput();
        rows=Integer.valueOf(inputs.get(0));
        columns=Integer.valueOf(inputs.get(1));
        x=new int[2][rows];
        for (int i=0;i<rows;i++){
            String[] temp = inputs.get((i+2)).split(" ");
            x[0][i]=Integer.valueOf(temp[0]);
            x[1][i]=Integer.valueOf(temp[1]);
        }

        gameManager.setFrameDuration(800);

        // La grille graphique et les jetons
        grille_graphique=new Rectangle[rows][columns];
        jetons_graphique=new Circle[2][rows];
        dim_cases=Math.min(Math.min(800/rows,1600/columns),100); // Second min pour ne pas avoir des cases trop grandes
        origines_x=960-columns*dim_cases/2;
        origines_y=540-rows*dim_cases/2;
        noms=new String[]{gameManager.getPlayer().getNicknameToken(),"Boss"};
        avatars=new String[]{gameManager.getPlayer().getAvatarToken(),"boss.png"};

        gameManager.setMaxTurns(rows*columns);
        gameManager.setTurnMaxTime(50);

        drawBackground();
        drawHud();
        drawGrids();
    }

    private void drawBackground() {
        graphicEntityModule.createSprite()
                .setImage("Background.jpg")
                .setAnchor(0);

    }

    private void drawGrids() {
        // Dessin de la grille
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {

                grille_graphique[i][j] = graphicEntityModule
                        .createRectangle()
                        .setWidth(dim_cases)
                        .setHeight(dim_cases)
                        .setX(origines_x + j * dim_cases)
                        .setY(origines_y + i * dim_cases)
                        .setLineWidth(1)
                        .setLineColor(0xc8c8c8)
                        .setFillColor(0xffffff);

            }
        }
        // Les jetons :
        for (int row=0;row<rows;row++) {
            for(int i=0;i<2;i++) {
                jetons_graphique[i][row] = graphicEntityModule
                        .createCircle()
                        .setX(origines_x + x[i][row] * dim_cases + dim_cases / 2)
                        .setY(origines_y + row * dim_cases + dim_cases / 2)
                        .setRadius(dim_cases/2-1)
                        .setFillColor(couleurs[i]);
            }
        }
    }

    private void drawHud() {
        for (int i=0;i<2;i++) {
            int x = i == 0 ? 200 : 1920 - 200;
            int y = 220;

            graphicEntityModule
                    .createRectangle()
                    .setWidth(140)
                    .setHeight(140)
                    .setX(x - 70)
                    .setY(y - 70)
                    .setLineWidth(0)
                    .setFillColor(couleurs[i]);

            graphicEntityModule
                    .createRectangle()
                    .setWidth(120)
                    .setHeight(120)
                    .setX(x - 60)
                    .setY(y - 60)
                    .setLineWidth(0)
                    .setFillColor(0xffffff);

            Text text = graphicEntityModule.createText(noms[i])
                    .setX(x)
                    .setY(y + 120)
                    .setZIndex(20)
                    .setFontSize(40)
                    .setFillColor(0xffffff)
                    .setAnchor(0.5);

            Sprite avatar = graphicEntityModule.createSprite()
                    .setX(x)
                    .setY(y)
                    .setZIndex(20)
                    .setImage(avatars[i])
                    .setAnchor(0.5)
                    .setBaseHeight(116)
                    .setBaseWidth(116);


        }
    }



    private void deplacer_jeton(int row, int col,int joueur){
        jetons_graphique[joueur][row].setX(origines_x + col * dim_cases + dim_cases / 2,Curve.EASE_IN_AND_OUT);
        x[joueur][row]=col;
    }





    @Override
    public void gameTurn(int turn) {
        if (turn%2==0) {// Si c'est au joueur de jouer
            player = gameManager.getPlayer();
            if (turn == 0) {// Premier tour de jeu
                player.sendInputLine(Integer.toString(rows));
                player.sendInputLine(Integer.toString(columns));
            }

            // Envoi des inputs
            for (int row = 0; row < rows; row++) {
                player.sendInputLine(Integer.toString(x[0][row])+" "+Integer.toString(x[1][row]));
            }

            player.execute();

            // Lecture des résultats du joueur
            try {
                final Action action = player.getAction();
                gameManager.addToGameSummary(String.format("Player %s moves his token in row %d to columns %d", action.player.getNicknameToken(), action.row, action.col));

                if (action.col <= x[0][action.row] || action.col >= x[1][action.row]) { // On vérifie que le jeton est sur une case valide
                    throw new InvalidAction("Invalid action.");
                }

                deplacer_jeton(action.row, action.col, 0);
                if (est_fini()){
                    gameManager.addToGameSummary(String.format("Player %s won !", action.player.getNicknameToken()));
                    gameManager.addTooltip(player,"You win !");
                    gameManager.winGame();
                }


            } catch (NumberFormatException e) {
                gameManager.addTooltip(player,"Wrong output!");
                gameManager.loseGame("Wrong output!");
            } catch (TimeoutException e) {
                gameManager.addTooltip(player,"Timeout !");
                gameManager.loseGame("Timeout !");
            } catch (InvalidAction | ArrayIndexOutOfBoundsException e) {
                gameManager.addTooltip(player,"Invalid action !");
                gameManager.loseGame("Invalid action !");
            } catch (Exception e) {
                gameManager.loseGame("Exception !");
            }
        } else { // Si c'est à l'IA de jouer
            // IA second joueur avec strategie gagnante
            Action reponse=jouer_IA();
            deplacer_jeton(reponse.row,reponse.col,1);
            gameManager.addToGameSummary(String.format("Boss moves his token in row %d to columns %d", reponse.row, reponse.col));
            if (est_fini()){
                gameManager.addToGameSummary(String.format("Boss won !%n"));
                gameManager.addTooltip(player,"Try again !");
                gameManager.loseGame("Try again !");
            }


        }



    }

    private Action jouer_IA(){
        // IA avec strategie gagnante

        // On traduit les distances entre deux pions en binaire (plus précisément en array de longueur 6 (car on ne dépassera pas 63) dans lequel on met l'ecriture binaire (inversée dans l'ordre) des longueurs).
        int[][] distances_bin=new int[rows][exp_max];
        int dist_max=0;
        int row_max=0;
        for (int row=0;row<rows;row++){
            int distance=x[1][row]-x[0][row]-1;
            if (distance>dist_max){
                dist_max=distance;
                row_max=row;
            }
            int curseur=0;
            while (distance>0){
                distances_bin[row][curseur]=distance%2;
                curseur++;
                distance=distance/2;
            }
            //System.err.printf("%d %s%n",distance,Arrays.toString(distances_bin[row])); //////
        }
        int[] parite=xor(distances_bin);
        //System.err.printf("Parité : %s %n",Arrays.toString(parite)); /////////////
        if (est_paire(parite)){ // Si on est dans une situation paire
            gameManager.addToGameSummary(String.format("Good choice !%n"));
            // dans ce cas on se déplace juste de 1 dans la colonne qui en possède le plus
            return new Action(player,row_max,x[1][row_max]-1);
        }else{ // Si on est dans une situation pas paire
            if(premiere_annonce){
                premiere_annonce=false;
                gameManager.addToGameSummary(String.format("You don't yet know but you have already lost !%n"));
            }
            // On cherche à quelle ligne on peut retirer ce qu'il faut pour retomber sur une config paire
            int[] reste=new int[exp_max];
            for(int row=0;row<rows;row++){
                reste=xor(new int[][]{parite,distances_bin[row]});
                if (est_superieur(distances_bin[row],reste)){
                    row_max=row;
                    break;
                }
            }

            // On renvoit la réponse
            return new Action(player,row_max,x[0][row_max]+bin_to_dec(reste)+1);
        }
    }

    private int[] xor(int[][] liste){
        // Renvoie la somme xor des éléments de la liste
        int[] resultat=new int[exp_max];
        for (int row=0;row<liste.length;row++){
            for (int i=0;i<exp_max;i++){
                resultat[i]=(resultat[i]+liste[row][i])%2;
            }
        }
        return resultat;
    }

    private boolean est_paire(int[] parite){
        // Renvoie si la situation est paire ou pas
        for (int i=0;i<exp_max;i++){
            if (parite[i]!=0){
                return false;
            }
        }
        return true;
    }

    private int bin_to_dec(int[] bin){
        // On retraduit en base 10
        int dec=0;
        for (int i=exp_max-1;i>=0;i--){
            dec=dec*2+bin[i];
        }
        return dec;
    }

    private boolean est_superieur(int[] bin1,int[] bin2){
        // Renvoie si l'entier bin1 ecrit en binaire est supérieur à  bin2
        for (int i=exp_max-1;i>=0;i--){
            if (bin1[i]>bin2[i]){return true;}
            if (bin1[i]<bin2[i]){return false;}
        }
        return true;// Si ils sont égaux

    }

    private boolean est_fini(){
        // Regarde s'il reste un coup jouable
        for (int row=0;row<rows;row++){
            if (x[0][row]+1<x[1][row]){
                return false;
            }
        }
        return true;
    }

}
