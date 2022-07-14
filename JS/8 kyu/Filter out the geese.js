// Write a function, gooseFilter / goose-filter / goose_filter /GooseFilter, that takes an array of strings as an argument and returns a filtered array containing the same elements but with the 'geese' removed.

const gooseFilter = (birds) => {
	let geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"];
	return birds.filter( elem => !geese.includes(elem) )
};