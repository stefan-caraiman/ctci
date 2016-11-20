var json_sample = require("./sample.json");

function hasUniqueChars(str) {
	if (str.length > 256) {
		return false;
	}
	else if (str.length <= 1) {
		return true;
	}
	else for (var i = 0; i < str.length; i++) {
		if (str.indexOf(str[i]) !== str.lastIndexOf(str[i]) || str.lastIndexOf(str[i]) !== i) {
			return false;
		}
	}
	return true;
}

for (var key in json_sample){
	console.log(hasUniqueChars(json_sample[key]));
}
