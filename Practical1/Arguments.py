# Arguments are objects which are referred by their top rule, the set of direct sub arguments, and its unique name (string). 
# We give below two examples of arguments

class Arguments:

    nameCount = 0

    def __init__(self, topRule, subArguments):
        self.topRule = topRule
        self.subArguments = subArguments
        Arguments.nameCount += 1
        self.name = "A" + str(Arguments.nameCount)

    def __eq__(self, other):
        return (self.topRule == other.topRule 
                and self.subArguments == other.subArguments 
                and self.name == other.name)

    # arguemtn example : $A_1: \rightarrow a$ == A1: -> a
    # argument example : $A_2: A_1 \Rightarrow c$ == A2: A2, A1 => c
    def __str__(self):
        argumentName = self.name + ": "
        argumentSubArgumentsList = []
        argumentSubArguments = ""
        argumentTopRule = self.topRule
        argumentImplication = ""

        # Extracting all sub arguments and putting them in a list
        for subArgument in self.subArguments:
            for argument in subArgument.setOfArguemnts():
                argumentSubArgumentsList.append(argument)

        # Extracting unique arguments from the list
        argumentSubArgumentsList = self.extractUniqueArguments(argumentSubArgumentsList)

        # Creating the string of unique sub arguments
        for argument in argumentSubArgumentsList:
            argumentSubArguments = argumentSubArguments + argument + ","

        if(argumentTopRule.isDefeasible):
            argumentImplication = "=> "
        else :
            argumentImplication = "->"
            
        return argumentName + argumentSubArguments + argumentImplication + str(argumentTopRule.conclusion)

    def __hash__(self):
        return hash((self.topRule, tuple(self.subArguments), self.name))

    @staticmethod
    def extractUniqueArguments(arguments):
        uniqueArguments = []

        for argument in arguments:
            if argument not in uniqueArguments:
                uniqueArguments.append(argument)

        return uniqueArguments


    def setOfArguemnts(self):
        allArguments = [self.name]

        for subArgument in self.subArguments:
            for argument in subArgument.setOfArguemnts():
                allArguments.append(argument)

        return self.extractUniqueArguments(allArguments)

