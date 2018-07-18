
/**
 * Create a table of contents for this document, and insert the tdm into
 * the document by replacing the node specified by the replace argument.
 **/
function tdm(replace, tdmHeadingLevel, minHeadingLevel, maxHeadingLevel) {

	// Global parameters

	// Create a link back to the contents
	var createBackLink = false;

	// Create a template for section number
	var sectionNoTemplate = document.createElement('span');
	sectionNoTemplate.className = 'section-no';

	// Create a template for a tdm entry number
	var tdmItemNoTemplate = document.createElement('span');
	tdmItemNoTemplate.className = 'tdm-item-no';

	// tdm heading level (i.e. 2 = h2, 3 = h3)

	if (!tdmHeadingLevel || tdmHeadingLevel < 1 || tdmHeadingLevel > 6) {
		var tdmHeadingLevel = 2;
	}

	if (!minHeadingLevel || minHeadingLevel < 1 || minHeadingLevel > maxHeadingLevel) {
		var minHeadingLevel = 2;
	}

	if (!maxHeadingLevel || maxHeadingLevel > 6 || maxHeadingLevel < minHeadingLevel) {
		var maxHeadingLevel = 6;
	}

	// Get the element node from the 'replace' id
	replace = document.getElementById(replace);

	// I18N

	// Label for the link back to the contents
	var backToContentsLabel = "retour";
	// Label for table of contents section
	var tdmLabel = "Table des matières";

	// Create a <div> element that is the root of the tdm tree
	var tdm = document.createElement("div");
	tdm.setAttribute('id','tdm');
 
	// Start the tdm with an anchor so we can link back to it

	var tdmHeadingNode = document.createElement('h' + tdmHeadingLevel);
	tdmHeadingNode.setAttribute('id','tdm-titre');
	tdmHeadingNode.appendChild(document.createTextNode(tdmLabel));
	tdm.appendChild(tdmHeadingNode);                   // Insert it
 
	// Create a <div> element that will hold the tdm and add it 
	var tdmBody = document.createElement("div");
	tdmBody.setAttribute('id','tdm-corps');
	tdm.appendChild(tdmBody);
 
	// Initialize an array that keeps track of section numbers
	var sectionNumbers = [0,0,0,0,0,0];

	// Recursively traverse the body of the document, looking for sections
	// sections marked with <h1>, <h2>, ... tags, and use them to create 
	// the tdm by adding rows to the table

	addSections(document.body, tdmBody, sectionNumbers);
 
	// Finally, insert the tdm into the document by replacing the node
	// specified by the replace argument with the tdm subtree

	replace.parentNode.replaceChild(tdm, replace);

	// This method recursively traverses the tree rooted at Node n, looking
	// looking for <h1> through <h6> tags, and uses the content of these tags
	// to build the table of contents by adding rows to the HTML table specified
	// by the tdm argument. It uses the sectionNumbers array to keep track of
	// the current section number.
	// This function is defined inside of maketdm(  ) so that it is not
	// visible from the outside. maketdm(  ) is the only function exported
	// by this JavaScript module.

	function addSections(n, tdm, sectionNumbers) {

		// Loop through all the children of n

		for(var m = n.firstChild; m != null; m = m.nextSibling) {

			// Check whether m is a heading element. It would be nice if we
			// could just use (m instanceof HTMLHeadingElement), but this is
			// not required by the specification and it does not work in IE.
			// Therefore, we must check the tagname to see if it is H1-H6.

			if ((m.nodeType == 1) &&  /* Node.ELEMENT_NODE */ 
				(m.tagName.length == 2) && (m.tagName.charAt(0) == "H")) {

				// Figure out what level heading it is

				var level = parseInt(m.tagName.charAt(1));

					//if (!isNaN(level) && (level >= 2) && (level <= 6)) {
					if (!isNaN(level) && (level >= minHeadingLevel) && (level <= maxHeadingLevel)) {

						var fragmentId = '';

						// Increment the section number for this heading level

						sectionNumbers[level-2]++;

						// And reset all lower heading-level numbers to zero

						for(var i = level - 1; i < 6; i++) sectionNumbers[i] = 0;

						// Now combine section numbers for all heading levels
						// to produce a section number like "2.3.1."

						var sectionNumber = "";
						for(var i = 0; i < level - 1; i++) {
							sectionNumber += sectionNumbers[i];
							if (i < level-1) sectionNumber += ".";
						}
 
						// Create an anchor to mark the beginning of this section
						// This will be the target of a link we add to the tdm
						// First, look if ther's already an id attribute

						if (m.getAttribute("id")) {
							fragmentId = m.getAttribute("id");
						} else {

							fragmentId = "SECT"+sectionNumber;
							m.setAttribute("id", fragmentId);
						}
 
						// Create a link back to the tdm and make it a
						// child of the anchor

						if (createBackLink) {
							var anchor = document.createElement("span");
							anchor.className = 'tdm-retour';
							var backlink = document.createElement("a");
							backlink.setAttribute("href", "#tdm");
							backlink.appendChild(document.createTextNode(backToContentsLabel));
							anchor.appendChild(backlink);
 
							// Insert the anchor into the document right before the
							// section header
							n.insertBefore(anchor, m);
						}
 
						// Now create a link to this section. It will be added
						// to the tdm below.

						var link = document.createElement("a");
						link.setAttribute("href", "#" + fragmentId);

						// Get the heading text using a function defined below

						var sectionTitle = getTextContent(m);

						// Use the heading text as the content of the link

						link.appendChild(document.createTextNode(sectionTitle));
 
						// Create a new entry for the tdm

						var tdmItem = document.createElement("div");
						tdmItem.className = 'tdm-item tdm-niveau-' + i;

						// Create two columns for the row

						var tdmItemEntry = document.createElement("span");
						tdmItemEntry.className = 'tdm-item-texte';

						tdmItemNoNode = tdmItemNoTemplate.cloneNode(false);
						tdmItemNoNode.appendChild(document.createTextNode(sectionNumber+" "));
						tdmItem.appendChild(tdmItemNoNode);

						// Put a link to the section in the second column
						tdmItemEntry.appendChild(link);

						// Add the columns to the row, and the row to the table
						//tdmItem.appendChild(tdmItemNumber);
						tdmItem.appendChild(tdmItemEntry);
						tdm.appendChild(tdmItem);
 
						// Modify the section header element itself to add
						// the section number as part of the section title

						sectionNumberNode = sectionNoTemplate.cloneNode(false);
						sectionNumberNode.appendChild(document.createTextNode(sectionNumber+" "));
						m.insertBefore(sectionNumberNode, m.firstChild);

						}
					}

					else {  // Otherwise, this is not a heading element, so recurse

						addSections(m, tdm, sectionNumbers);
					}
				}
			}
 
			// This utility function traverses Node n, returning the content of
			// all Text nodes found and discarding any HTML tags. This is also
			// defined as a nested function, so it is private to this module.

			function getTextContent(n) {
				var s = '';
				var children = n.childNodes;
				for(var i = 0; i < children.length; i++) {
					var child = children[i];
					if (child.nodeType == 3 /*Node.TEXT_NODE*/) s += child.data;
					else s += getTextContent(child);
				}
				return s;
			}
		}