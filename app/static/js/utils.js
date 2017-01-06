var utils = {
    getAvailableMunicipalities: function() {
        return [
            "Čačak",
            "Inđija",
            "Kraljevo",
            "Loznica",
            "Novi Beograd",
            "Pripolje",
            "Sombor",
            "Valjevo",
            "Vranje",
            "Zvezdara"

        ]
    },

     getAvailableYearsParlamentarni: function() {
        return [
            "2003",
            "2008",
            "2012",
            "2014",
        ]
    },
 getAvailableYearsPresidential: function() {
        return [
            "2002",
            "2003",
            "2004",
            "2008",
            "2012",
        ]
    },
    getAvailableBudgetTypes: function() {
        return [
            "Expenditures",
            "Revenues"
        ]
    },
  getAvailableElectionTypes: function() {
        return [
            "Predsednicki",
            "Parlamentarni"
        ]
    },
    getRandomMunicipality: function(){
        var muniIdx = Math.floor(Math.random() * utils.getAvailableMunicipalities().length);
        return utils.getAvailableMunicipalities()[muniIdx];
    },
     getRandomYearsParlamentarni: function(){
        var muniIdx = Math.floor(Math.random() * utils.getAvailableYearsParlamentarni().length);
        return utils.getAvailableYearsParlamentarni()[muniIdx];
    },
    getRandomYearsPresidential: function(){
        var muniIdx = Math.floor(Math.random() * utils.getAvailableYearsPresidential().length);
        return utils.getAvailableYearsPresidential()[muniIdx];
    },

    getRandomBudgetType: function(){
        var btIdx = Math.floor(Math.random() * utils.getAvailableBudgetTypes().length);
        return utils.getAvailableBudgetTypes()[btIdx];
    },

   getRandomElectionType: function(){
        var btIdx = Math.floor(Math.random() * utils.getAvailableElectionTypes().length);
        return utils.getAvailableElectionTypes()[btIdx];
    },
    getURLParameter: function(name){
        var results = new RegExp('[\?&]' + name + '=([^&#]*)').exec(window.location.href);
        if (results==null){
           return null;
        }
        else{
           return results[1] || 0;
        }
    }
};