import pickle

gramatika = [
    ['Tu krabic_ polož sem.', "i"],
    ['Četl jsem všechny jeho novel_.', "y"],
    ['Až půjdeš spát, vypni televiz_.', "i"],
    ['Lupič ukradl z kas_ dva tisíce.', "y"],
    ['V láhv_ zbylo ještě trochu vína.', "i"],
    ['Kup v papírnictví balicí papír a žlutou mašl_.', "i"],
    ['Na stole byly tácy s chlebíčky a jednohubkam_.', "i"],
    ['Počkej na mě, prosím, chvíl_.', "i"],
    ['V klec_ sedělo několik pestrobarevných papoušků.', "i"],
    ['Sedím v poslední lavic_ u dveří.', "i"],
    ['Počkám na tebe na hráz_.', "i"]
]

pickle.dump(gramatika, open("data.dat", "wb"))
