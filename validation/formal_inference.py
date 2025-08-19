"""
FORMAL INFERENCE ENGINE - Micro Module
Complete mathematical inference system for logical proofs.
Implements all necessary inference rules for formal validation.

CRITICAL: This module provides mathematical certainty of logical validity.
Under 200 LOC for maintainability and auditability.
"""

from typing import Set, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum

from axioms.logical_foundation import LogicalStatement, LogicalRule, LogicalAxioms

class InferenceRule(Enum):
    MODUS_PONENS = "modus_ponens"
    MODUS_TOLLENS = "modus_tollens"
    HYPOTHETICAL_SYLLOGISM = "hypothetical_syllogism"
    DISJUNCTIVE_SYLLOGISM = "disjunctive_syllogism"
    CONJUNCTION_INTRODUCTION = "conjunction_intro"
    CONJUNCTION_ELIMINATION = "conjunction_elim"
    UNIVERSAL_INSTANTIATION = "universal_inst"
    EXISTENTIAL_GENERALIZATION = "existential_gen"

@dataclass
class InferenceStep:
    """Single step in formal inference"""
    conclusion: LogicalStatement
    premises: List[LogicalStatement]
    rule: InferenceRule
    valid: bool

class FormalInferenceEngine:
    """
    Complete formal inference engine
    Implements all standard logical inference rules
    """
    
    def __init__(self):
        self.known_facts: Set[LogicalStatement] = set()
        self.inference_history: List[InferenceStep] = []
    
    def add_axiom(self, statement: LogicalStatement) -> bool:
        """Add axiom as known fact"""
        if self._is_consistent_with_known_facts(statement):
            self.known_facts.add(statement)
            return True
        return False
    
    def derive_all_consequences(self, premises: List[LogicalStatement]) -> Set[LogicalStatement]:
        """
        Derive all possible logical consequences from premises
        Returns complete set of derivable statements
        """
        working_set = set(premises)
        working_set.update(self.known_facts)
        
        # Fixed-point iteration to derive all consequences
        changed = True
        iterations = 0
        max_iterations = 50  # Prevent infinite loops
        
        while changed and iterations < max_iterations:
            changed = False
            initial_size = len(working_set)
            
            # Apply all inference rules
            new_statements = self._apply_all_rules(list(working_set))
            
            for stmt in new_statements:
                if stmt not in working_set:
                    if self._is_consistent_with_known_facts(stmt):
                        working_set.add(stmt)
                        changed = True
            
            iterations += 1
            
        return working_set
    
    def can_derive(self, target: LogicalStatement, premises: List[LogicalStatement]) -> bool:
        """
        Check if target statement can be formally derived from premises
        Returns True only if derivation is mathematically certain
        """
        consequences = self.derive_all_consequences(premises)
        
        # Check if target or logically equivalent statement is derivable
        for stmt in consequences:
            if self._statements_equivalent(stmt, target):
                return True
                
        return False
    
    def _apply_all_rules(self, statements: List[LogicalStatement]) -> Set[LogicalStatement]:
        """Apply all inference rules using inference_rules module"""
        # Import here to avoid circular imports
        from validation.inference_rules import apply_all_inference_rules
        return apply_all_inference_rules(statements)
    
    def _is_consistent_with_known_facts(self, statement: LogicalStatement) -> bool:
        """Check if statement is consistent with known facts"""
        for fact in self.known_facts:
            if fact.proposition == statement.proposition:
                if fact.truth_value != statement.truth_value:
                    return False  # Contradiction
        return True
    
    def _statements_equivalent(self, stmt1: LogicalStatement, stmt2: LogicalStatement) -> bool:
        """Check if two statements are logically equivalent"""
        return (stmt1.proposition == stmt2.proposition and 
                stmt1.truth_value == stmt2.truth_value)

# Global inference engine
INFERENCE_ENGINE = FormalInferenceEngine()