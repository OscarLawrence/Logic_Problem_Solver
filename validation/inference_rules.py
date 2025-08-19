"""
INFERENCE RULES - Micro Module
Implementation of standard logical inference rules.
Provides the mathematical foundation for formal proofs.

CRITICAL: This module implements mathematically sound inference.
Under 200 LOC for maintainability and auditability.
"""

from typing import Set, List, Tuple
from axioms.logical_foundation import LogicalStatement
from validation.formal_inference import InferenceRule, InferenceStep

class InferenceRuleImplementations:
    """
    Implementation of all standard logical inference rules
    Each rule is mathematically validated
    """
    
    @staticmethod
    def apply_modus_ponens(statements: List[LogicalStatement]) -> Set[LogicalStatement]:
        """Apply modus ponens rule: P, P→Q ⊢ Q"""
        new_statements = set()
        
        for i, stmt1 in enumerate(statements):
            for j, stmt2 in enumerate(statements):
                if i != j and InferenceRuleImplementations._is_implication(stmt2):
                    antecedent, consequent = InferenceRuleImplementations._parse_implication(stmt2)
                    if stmt1.proposition == antecedent and stmt1.truth_value:
                        derived = LogicalStatement(consequent, True)
                        new_statements.add(derived)
        
        return new_statements
    
    @staticmethod
    def apply_modus_tollens(statements: List[LogicalStatement]) -> Set[LogicalStatement]:
        """Apply modus tollens rule: ¬Q, P→Q ⊢ ¬P"""
        new_statements = set()
        
        for i, stmt1 in enumerate(statements):
            for j, stmt2 in enumerate(statements):
                if i != j and InferenceRuleImplementations._is_implication(stmt2):
                    antecedent, consequent = InferenceRuleImplementations._parse_implication(stmt2)
                    if stmt1.proposition == consequent and not stmt1.truth_value:
                        derived = LogicalStatement(antecedent, False)
                        new_statements.add(derived)
        
        return new_statements
    
    @staticmethod
    def apply_hypothetical_syllogism(statements: List[LogicalStatement]) -> Set[LogicalStatement]:
        """Apply hypothetical syllogism rule: P→Q, Q→R ⊢ P→R"""
        new_statements = set()
        
        for i, stmt1 in enumerate(statements):
            for j, stmt2 in enumerate(statements):
                if i != j and InferenceRuleImplementations._is_implication(stmt1) and InferenceRuleImplementations._is_implication(stmt2):
                    ant1, cons1 = InferenceRuleImplementations._parse_implication(stmt1)
                    ant2, cons2 = InferenceRuleImplementations._parse_implication(stmt2)
                    
                    if cons1 == ant2:  # P→Q, Q→R
                        derived_prop = f"{ant1}→{cons2}"
                        derived = LogicalStatement(derived_prop, True)
                        new_statements.add(derived)
        
        return new_statements
    
    @staticmethod
    def apply_conjunction_introduction(statements: List[LogicalStatement]) -> Set[LogicalStatement]:
        """Apply conjunction introduction: P, Q ⊢ P∧Q"""
        new_statements = set()
        
        for i, stmt1 in enumerate(statements):
            for j, stmt2 in enumerate(statements):
                if i < j and stmt1.truth_value and stmt2.truth_value:
                    conj_prop = f"{stmt1.proposition}∧{stmt2.proposition}"
                    derived = LogicalStatement(conj_prop, True)
                    new_statements.add(derived)
        
        return new_statements
    
    @staticmethod
    def apply_disjunctive_syllogism(statements: List[LogicalStatement]) -> Set[LogicalStatement]:
        """Apply disjunctive syllogism: P∨Q, ¬P ⊢ Q"""
        new_statements = set()
        
        for i, stmt1 in enumerate(statements):
            for j, stmt2 in enumerate(statements):
                if i != j and "∨" in stmt1.proposition:
                    # Parse disjunction P∨Q
                    parts = stmt1.proposition.split("∨")
                    if len(parts) == 2:
                        left_prop = parts[0].strip()
                        right_prop = parts[1].strip()
                        
                        # Check if we have ¬P
                        if stmt2.proposition == left_prop and not stmt2.truth_value:
                            derived = LogicalStatement(right_prop, True)
                            new_statements.add(derived)
                        # Check if we have ¬Q
                        elif stmt2.proposition == right_prop and not stmt2.truth_value:
                            derived = LogicalStatement(left_prop, True)
                            new_statements.add(derived)
        
        return new_statements
    
    @staticmethod
    def _is_implication(statement: LogicalStatement) -> bool:
        """Check if statement is implication"""
        return "→" in statement.proposition or "implies" in statement.proposition
    
    @staticmethod
    def _parse_implication(statement: LogicalStatement) -> Tuple[str, str]:
        """Parse implication into antecedent and consequent"""
        if "→" in statement.proposition:
            parts = statement.proposition.split("→")
        else:
            parts = statement.proposition.split("implies")
        return parts[0].strip(), parts[1].strip()

# Export the rule implementations
def apply_all_inference_rules(statements: List[LogicalStatement]) -> Set[LogicalStatement]:
    """Apply all inference rules to derive new statements"""
    new_statements = set()
    
    # Apply each rule
    new_statements.update(InferenceRuleImplementations.apply_modus_ponens(statements))
    new_statements.update(InferenceRuleImplementations.apply_modus_tollens(statements))
    new_statements.update(InferenceRuleImplementations.apply_hypothetical_syllogism(statements))
    new_statements.update(InferenceRuleImplementations.apply_conjunction_introduction(statements))
    new_statements.update(InferenceRuleImplementations.apply_disjunctive_syllogism(statements))
    
    return new_statements

def is_implication(statement: LogicalStatement) -> bool:
    """Check if statement is an implication"""
    return InferenceRuleImplementations._is_implication(statement)

def parse_implication(statement: LogicalStatement) -> Tuple[str, str]:
    """Parse implication statement"""
    return InferenceRuleImplementations._parse_implication(statement)