import bibtexparser
with open('bib/tastwo.bib', 'r') as fh:
    tastwolib = bibtexparser.load(fh)
with open('bib/CuBr2.bib', 'r') as fh:
    cubr2lib = bibtexparser.load(fh)
with open('bib/cmb.bib', 'r') as fh:
    cmblib = bibtexparser.load(fh)
with open('bib/Thesis.bib', 'r') as fh:
    thesislib = bibtexparser.load(fh)j


fixes = [
    [
        tastwolib,
        'bovet_pseudogapped_2004',
        'title',
        '{Pseudogapped {Fermi} surfaces of 1{T}-\ce{TaS2} and 1{T}-\ce{TaSe2}: {A} charge density wave effect}',
    ],
    [
        tastwolib,
        'heinz_study_1985',
        'title',
        '{Study of \ce{Si}(111) Surfaces by Optical Second-Harmonic Generation: Reconstruction and Surface Phase Transformation}',
    ],
    [
        tastwolib,
        'teo2008',
        'title',
        '{Surface states and topological invariants in three-dimensional topological insulators: Application to \ce{Bi_{1-x}Sb_x}}',
    ],
    [
        cubr2lib,
        'essler_quasi-one-dimensional_1997',
        'title',
        '{Quasi-one-dimensional spin-1/2 {H}eisenberg magnets in their ordered phase: {C}orrelation functions}',
    ],
    [
        cubr2lib,
        'wang_nmr_2018',
        'title',
        '{{NMR} evidence of charge fluctuations in multiferroic \ce{CuBr2}',
    ],
    [
        cubr2lib,
        'furukawa_ground-state_2012',
        'title',
        '{Ground-state phase diagram of a spin-1/2 frustrated ferromagnetic {XXZ} chain: {H}aldane dimer phase and gapped/gapless chiral phases}',
    ],
    [
        cubr2lib,
        'lebernegg_magnetism_2013',
        'title',
        '{Magnetism of \ce{CuX2} frustrated chains (X = F, Cl, Br): the role of covalency}',
    ],
    [
        cubr2lib,
        'lee_investigation_2012',
        'title',
        '{Investigation of the spin exchange interactions and the magnetic structure of the high-temperature multiferroic \ce{CuBr2}}',
    ],
    [
        tastwolib,
        'mann_probing_2016',
        'title',
        '{Probing the coupling between a coublon excitation and the charge-density wave in \ce{TaS2} by ultrafast optical spectroscopy}',
    ],
    [
        tastwolib,
        'wu_hexagonal_1989',
        'title',
        '{Hexagonal {Domain}-{Like} {Charge} {Density} {Wave} {Phase} of \ce{TaS2} {Determined} by {Scanning} {Tunneling} {Microscopy}}',
    ],
    [
        cubr2lib,
        'measson_amplitude_2014',
        'title',
        '{Amplitude {H}iggs mode in the 2{H}-\ce{NbSe2} superconductor}',
    ],
    [
        cubr2lib,
        'zhang_giant_2020',
        'title',
        '{Giant pressure-enhancement of multiferroicity in \ce{CuBr2}}',
    ],
    [
        cubr2lib,
        'zhao_cubr2_2012',
        'title',
        '{\ce{CuBr2} - {A} {New} {Multiferroic} {Material} with {High} {Critical} {Temperature}}',
    ],
    [
        thesislib,
        'petersen_nonlinear_2006',
        'title',
        '{Nonlinear optical signature of the tensor order in \ce{Cd2Re2O7}}',
    ],
    [
        cubr2lib,
        'ruegg_quantum_2008',
        'title',
        '{Quantum {M}agnets under {P}ressure: {C}ontrolling {E}lementary {E}xcitations in \ce{TlCuCl3}}',
    ],
    [
        thesislib,
        'sie_valley-selective_2015',
        'title',
        '{Valley-selective optical {S}tark effect in monolayer \ce{WS2}}',
    ],
    [
        thesislib,
        'wang_axial_2022',
        'title',
        '{Axial {Higgs} mode detected by quantum pathway interference in \ce{RTe3}}',
    ],
    [
        thesislib,
        'wilson_renormalization_1974',
        'title',
        'The renormalization group and the $\epsilon$ expansion',
    ],
]






















