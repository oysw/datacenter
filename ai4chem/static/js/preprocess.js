let structureFeaturizers = [
    "DensityFeatures",
    "GlobalSymmetryFeatures",
    "Dimensionality",
    "RadialDistributionFunction",
    "PartialRadialDistributionFunction",
    "ElectronicRadialDistributionFunction",
    "CoulombMatrix",
    "SineCoulombMatrix",
    "OrbitalFieldMatrix",
    "MinimumRelativeDistances",
    "SiteStatsFingerprint",
    "EwaldEnergy",
    "BondFractions",
    "BagofBonds",
    "StructuralHeterogeneity",
    "MaximumPackingEfficiency",
    "ChemicalOrdering",
    "XRDPowderPattern",
    "CGCNNFeaturizer",
    "JarvisCFID",
    "SOAP",
    "GlobalInstabilityIndex"
];
let compositionFeaturizers = [
    "OxidationStates",
    "AtomicOrbitals",
    "BandCenter",
    "ElectronegativityDiff",
    "ElectronAffinity",
    "Stoichiometry",
    "ValenceOrbital",
    "IonProperty",
    "ElementFraction",
    "TMetalFraction",
    "CohesiveEnergy",
    "Miedema",
    "YangSolidSolution",
    "AtomicPackingEfficiency"
];
let siteFeaturizers = [
    "AGNIFingerprints",
    "OPSiteFingerprint",
    "CrystalNNFingerprint",
    "VoronoiFingerprint",
    // "ChemicalSRO",
    "GaussianSymmFunc",
    "EwaldSiteEnergy",
    "ChemEnvSiteFingerprint",
    "CoordinationNumber",
    "GeneralizedRadialDistributionFunction",
    "AngularFourierSeries",
    "LocalPropertyDifference",
    "BondOrientationalParameter",
    "SiteElementalProperty",
    "AverageBondLength",
    "AverageBondAngle"
];
let localEnvCalculator = [
    "BrunnerNN_real",
    "BrunnerNN_reciprocal",
    "BrunnerNN_relative",
    "CovalentBondNN",
    "Critic2NN",
    "CrystalNN",
    "CutOffDictNN",
    "EconNN",
    "JmolNN",
    "MinimumDistanceNN",
    "MinimumOKeeffeNN",
    "MinimumVIRENN",
    "OpenBabelNN",
    "VoronoiNN"
];


function compositionFeaturizersSelector() {
    let html_str = "<option>None</option>";
    for (let i = 0; i < compositionFeaturizers.length; i++){
        let featurizers = compositionFeaturizers[i];
        html_str += '<option value=' + featurizers + '>' + featurizers + '</option>';
    }
    return html_str
}

function structureFeaturizersSelector() {
    let html_str = "<option>None</option>";
    for (let i = 0; i < structureFeaturizers.length; i++){
        let featurizers = structureFeaturizers[i];
        html_str += '<option value=' + featurizers + '>' + featurizers + '</option>';
    }
    return html_str
}