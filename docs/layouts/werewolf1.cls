layout {
    size: 2.5in, 3.5in
}

export {
    output: cards
    bulk {
        name: [role][repeat-index].png
    }
}

macros {
    dark-red = #a32b1d
}

role-border {
    type: rect
    position: center, .5in
    size: 1.5in, .25in
    corner-radius: .1in
}

role {
    type: text
    position: center, .5in
    size: 1.5in, .25in
    font: 12pt, Palatino Linotype
    font-color: [if| [eq| [role] | werewolf ] | [dark-red] | black ]
    align: center, middle
    text: [capitalize| [role] ]
}

icon {
    type: image
    position: center, 1in
    source: images/[role].png
}

data {
repeat, role
2, werewolf
1, seer
4, villager
}