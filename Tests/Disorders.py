# File: Disorders.py

class Anxiety() :
    #Represents anxiety Disorders

    def __init__(self) :
        self.num_symptoms = 0
        self.name = "Anxiety"
        self.words = [  "aversion", "avoidance", "avoiding", "avoided", "critical", "overwhelm", 
                        "overwhelming","powerless", "worried", "worrying", "worry" , "withdrawing",
                        "scared", "panic", "panicking", "restless", "restlessness", "tension", "tense",
                        "agitated", "agitation", "anxiousness", "apprehension", "apprehensiveness", "fear",
                        "unease", "uneasiness", "nervousness", "nerves", "strain", "alarm", "anguish",
                        "discomfort", "shaky", "trembling", "jittery", "jitters", "timid", "timidity", 
                        "stressed", "stress"]
        self.word_cut_off = 2
        self.symptoms = [   "Do you feel restless, keyed up, or on edge?",
                            "Have you felt easily fatigued recently?",
                            "Do you have difficulties concentrating, or does your mind often go blank?",
                            "Have you felt irritable recently?",
                            "Have you experienced muscle tension recently?",
                            "Have you had trouble falling or staying asleep?"]
        self.cut_off = 3
        self.end_message = "https://www.heretohelp.bc.ca/infosheet/anxiety-disorders#cure"

class Depression() :
    # Represents depression disorders

    def __init__(self) :
        self.num_symptoms = 0
        self.name = "Depression"
        self.words = [  "abandoned", "abandon", "abandoning", "depressed", "depression", "depressing",
                        "sad", "down", "unmotivated","unmotivating", "uninterested", "sleepy", "groggy","restless",
                        "blue", "fatigued", "indecisive","worthless", "guilty","suicidal", "alienated", 
                        "alienating", "apathetic", "ashamed", "despair", "disapproving", "disillusioned",
                        "dismayed", "distant", "empty", "humiliated", "humiliating", "ignored", "inadequate",
                        "indifferent", "inferior", "insecure", "insignificant", "isolated", "isolating", "isolate",
                        "loathing", "lonely", "powerless", "rejected", "rejects", "reject", "resentful", "ridiculed",
                        "victimized", "withdrawn", "withdrawing" ]
        self.word_cut_off = 2
        self.symptoms = [ "Have you experienced depressed mood recently?",
                          "Have you recently lost interest in activities you once found compelling?",
                          "Have you recently experienced a lack or excess of sleep?",
                          "Have you recently experienced weight loss or gain or a change in appetite",
                          "Have you recently experienced reduced movement or movement with no purpose?",
                          "Do you feel indecisive or find yourself unable to concentrate?",
                          "Do you feel worthless or guilty?",
                          "Do you recurrently think of death or suicide?"]
        self.cut_off = 5
        self.end_message = "https://www.skylandtrail.org/Our-Expertise/Diagnoses/Depression?gclid=EAIaIQobChMI7bKy9Kne4gIVmNlkCh32bgwLEAAYAyAAEgIYf_D_BwE"

class OCD() :
    # Represents depression disorders
    def __init__(self) :
        self.num_symptoms = 0
        self.name = "Obsession Compulsive Disorder"
        self.words = [ "obsession", "obsess", "obsessed","compulsive","compulsion", "required", "control",
                       "perfectionist", "symmetry", "exactness", "exact", "symmetric", "hyperfocus", "hyperfocused",
                       "must", "compelled", "contaminated", "contamination", "dirty", "disgusting", "clean",
                       "cleaning", "spotless", "cleaned", "filthy"]
        self.word_cut_off = 2
        self.symptoms = [   "Do you have persistent thoughts, urges or impulses that are unwanted and cause anxiety?",
                            "If you answered yes to the previous question, do you attempt to supress these thoughts with some other thought or action?",
                            "Do you perform repetitive behavior or mental acts in response to an obsession or rule?",
                            "If you answered yes to the previous question, do you perform these behaviors to prevent or reduce anxiety?"]
        self.cut_off = 3
        self.end_message = "https://iocdf.org/about-ocd/"

class PTSD() :
    # Represents depression disorders

    def __init__(self) :
        self.num_symptoms = 0
        self.name = "Post Traumatic Stress Disorder"
        self.words = [  "traumatized", "vigilant", "avoid", "avoiding", "flashback", "flashbacks", "trauma",
                        "scared", "scary", "fear", "fearful", "jumpy", "startled", "startle", "war"]
        self.word_cut_off = 2
        self.symptoms = [   "Have you been directly exposed to a trauma or learned of a trauma that happened to someone you know?",
                            "Do you have recurrent memories, dreams, or flashbacks of a traumatic event?",
                            "Do you avoid thinking about a traumatic event?",
                            "Do you avoid people, places or activities that remind you of a traumatic experience?",
                            "Have you experienced a negative emotional state, loss of interest, or social withdrawal recently?",
                            "Have you been irritable, wreckless, hypervigilant, or restless recently?"]
        self.cut_off = 4
        self.end_message = "https://www.nimh.nih.gov/health/topics/post-traumatic-stress-disorder-ptsd/index.shtml"

class BPD() :
    # Represents Bipolar disorders

    def __init__(self) :
        self.num_symptoms = 0
        self.name = "Bipolar Disorder"
        self.words = [  "energetic", "talkative", "distracted", "nonstop", "risky", "impulsive",
                        "uncontrollable", "energy", "uncontrolled", "risking", "impulse", "highs",
                        "lows", "mania", "irritability", "insomnia", "sleepy", "euphoric", "sad",
                        "high", "low", "manic", "distracting", "energy"]
        self.word_cut_off = 2
        self.symptoms = [   "Have you experienced inflated self esteem or grandiosity recently?",
                            "Have you experienced a decreased need for sleep recently?",
                            "Have you experienced pressured speech or being more talkative than usual?",
                            "Have you experienced racing thoughts recently?",
                            "Do you feel as if you are easily distractable recently?",
                            "Have you experienced an increase in goal directed activity recently?",
                            "Do you get involved in activities with a potential for painful consequences?"]
        self.cut_off = 3
        self.end_message = "https://www.nimh.nih.gov/health/topics/bipolar-disorder/index.shtml"
