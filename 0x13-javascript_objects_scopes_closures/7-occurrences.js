#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, search) => search === searchElement ? count + 1 : count, 0);
};
