var utils = {
    getAvailableMunicipalities: function() {
        return [
            "Čačak",
            "Inđija",
            "Kraljevo",
            "Loznica",
            "Novi Beograd",
            "Pripolje",
            "Valjevo",
            "Vranje",
            "Zvezdara"
        ]
    },

    getAvailableBudgetTypes: function() {
        return [
            "Expenditures",
            "Revenues"
        ]
    },

    getRandomMunicipality: function(){
        var muniIdx = Math.floor(Math.random() * utils.getAvailableMunicipalities().length);
        return utils.getAvailableMunicipalities()[muniIdx];
    },

    getRandomBudgetType: function(){
        var btIdx = Math.floor(Math.random() * utils.getAvailableBudgetTypes().length);
        return utils.getAvailableBudgetTypes()[btIdx];
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