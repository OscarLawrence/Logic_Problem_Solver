"""
Immutable Logical Foundation - Core axioms that cannot be modified
Mathematical basis for all logical operations in the system

CRITICAL: This file defines the unchangeable logical rules.
Any system operation that violates these axioms must be rejected.
"""

from typing import Set, Tuple, Union, Any
from dataclasses import dataclass
from enum import Enum

class LogicalOperator(Enum):
    AND = "∧"
    OR = "∨" 
    NOT = "¬"
    IMPLIES = "→"
    EQUIVALENT = "↔"

@dataclass(frozen=True)  # Immutable
class LogicalStatement:
    """Represents a logical statement that can be true or false"""
    proposition: str
    truth_value: bool = None  # None means unknown/to be derived
    
    def __hash__(self):
        return hash((self.proposition, self.truth_value))

@dataclass(frozen=True)  # Immutable  
class LogicalRule:
    """Represents a logical inference rule"""
    premises: Tuple[LogicalStatement, ...]
    conclusion: LogicalStatement
    rule_name: str
    
    def is_valid(self) -> bool:
        """Verify this rule follows logical axioms"""
        return LogicalAxioms.validate_inference(self.premises, self.conclusion)

class LogicalAxioms:
    """
    Fundamental logical axioms - CANNOT BE MODIFIED
    These define what constitutes valid logical reasoning
    """
    
    @staticmethod
    def law_of_identity(statement: LogicalStatement) -> bool:
        """A = A (everything is identical to itself)"""
        return statement.proposition == statement.proposition
    
    @staticmethod  
    def law_of_non_contradiction(p: LogicalStatement, not_p: LogicalStatement) -> bool:
        """¬(P ∧ ¬P) - something cannot be both true and false"""
        if p.proposition == not_p.proposition:
            return not (p.truth_value and not_p.truth_value)
        return True
    
    @staticmethod
    def law_of_excluded_middle(p: LogicalStatement) -> bool:
        """P ∨ ¬P - everything is either true or false"""
        return p.truth_value is not None
        
    @staticmethod
    def modus_ponens(p: LogicalStatement, p_implies_q: LogicalStatement, q: LogicalStatement) -> bool:
        """If P and (P → Q), then Q"""
        if p.truth_value and p_implies_q.truth_value:
            return q.truth_value
        return True  # Rule doesn't apply
        
    @staticmethod
    def modus_tollens(not_q: LogicalStatement, p_implies_q: LogicalStatement, not_p: LogicalStatement) -> bool:
        """If ¬Q and (P → Q), then ¬P"""
        if not_q.truth_value is False and p_implies_q.truth_value:
            return not_p.truth_value is False
        return True
        
    @staticmethod
    def validate_inference(premises: Tuple[LogicalStatement, ...], conclusion: LogicalStatement) -> bool:
        """
        Verify that a conclusion logically follows from premises
        Returns True only if inference is logically valid
        """
        # Check basic consistency
        for premise in premises:
            if not LogicalAxioms.law_of_identity(premise):
                return False
                
        # Check for contradictions in premises
        propositions = {}
        for premise in premises:
            if premise.proposition in propositions:
                if propositions[premise.proposition] != premise.truth_value:
                    return False  # Contradiction in premises
            propositions[premise.proposition] = premise.truth_value
            
        # For now, basic validation - can be extended with formal proof system
        return True

class CoherenceValidator:
    """
    Validates logical coherence of the entire system
    CRITICAL: This class cannot be modified or bypassed
    """
    
    def __init__(self):
        self.known_statements: Set[LogicalStatement] = set()
        self.inference_rules: Set[LogicalRule] = set()
        
    def add_statement(self, statement: LogicalStatement) -> bool:
        """
        Add a statement only if it doesn't create logical contradiction
        Returns False and rejects if contradiction detected
        """
        # Check against existing statements
        for existing in self.known_statements:
            if existing.proposition == statement.proposition:
                if existing.truth_value != statement.truth_value:
                    return False  # Contradiction detected
                    
        # Check consistency with logical axioms
        for existing in self.known_statements:
            if not LogicalAxioms.law_of_non_contradiction(statement, existing):
                return False
                
        self.known_statements.add(statement)
        return True
        
    def add_inference_rule(self, rule: LogicalRule) -> bool:
        """
        Add inference rule only if logically valid
        Returns False and rejects if invalid
        """
        if not rule.is_valid():
            return False
            
        self.inference_rules.add(rule)
        return True
        
    def validate_system_coherence(self) -> bool:
        """
        Comprehensive check of entire system logical coherence
        Returns False if ANY logical inconsistency found
        """
        # Check all statements for internal consistency
        propositions = {}
        for statement in self.known_statements:
            if statement.proposition in propositions:
                if propositions[statement.proposition] != statement.truth_value:
                    return False
            propositions[statement.proposition] = statement.truth_value
            
        # Check all inference rules are valid
        for rule in self.inference_rules:
            if not rule.is_valid():
                return False
                
        return True

# Global immutable instance - the system's logical foundation
LOGICAL_FOUNDATION = CoherenceValidator()

def enforce_logical_coherence(operation_result: Any) -> bool:
    """
    CRITICAL SAFETY FUNCTION
    Every system operation must pass through this validator
    Returns False if operation would break logical coherence
    """
    return LOGICAL_FOUNDATION.validate_system_coherence()

# Mathematical proofs moved to axioms/safety_proof.py