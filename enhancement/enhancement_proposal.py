"""
ENHANCEMENT PROPOSAL - Micro Module
Represents and validates individual enhancement proposals.
Provides comprehensive safety validation for code changes.

CRITICAL: This module validates all proposed system modifications.
Under 200 LOC for maintainability and auditability.
"""

import ast
from typing import Any, Optional

from axioms.logical_foundation import LogicalStatement
from guardrails.logic_enforcer import validate_system_modification
from validation.coherence_proof import COHERENCE_PROOF_SYSTEM

class EnhancementProposal:
    """Represents a proposed system enhancement"""
    
    def __init__(self, name: str, description: str, code: str, target_module: str):
        self.name = name
        self.description = description
        self.code = code
        self.target_module = target_module
        self.safety_validated = False
        self.coherence_proof: Optional[Any] = None
        
    def validate_safety(self) -> bool:
        """
        Comprehensive safety validation of enhancement proposal
        Returns True only if enhancement is provably safe
        """
        # Step 1: Static code analysis
        if not self._validate_code_safety():
            return False
            
        # Step 2: Formal coherence proof
        if not self._generate_coherence_proof():
            return False
            
        # Step 3: Protected component check
        if not validate_system_modification("enhancement", self.target_module):
            return False
            
        self.safety_validated = True
        return True
        
    def _validate_code_safety(self) -> bool:
        """Validate enhancement code cannot compromise safety systems"""
        try:
            # Parse code to AST for analysis
            tree = ast.parse(self.code)
            
            # Check for dangerous operations
            for node in ast.walk(tree):
                # Block attempts to modify safety-critical modules
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        if self._is_protected_module(alias.name):
                            return False
                            
                if isinstance(node, ast.ImportFrom):
                    if self._is_protected_module(node.module):
                        return False
                        
                # Block direct variable assignments to safety systems
                if isinstance(node, ast.Assign):
                    for target in node.targets:
                        if isinstance(target, ast.Name):
                            if self._is_protected_variable(target.id):
                                return False
                                
                # Block function calls that could compromise safety
                if isinstance(node, ast.Call):
                    if isinstance(node.func, ast.Name):
                        if self._is_dangerous_function(node.func.id):
                            return False
                            
            return True
            
        except SyntaxError:
            return False  # Invalid code
            
    def _is_protected_module(self, module_name: str) -> bool:
        """Check if module is safety-critical and protected"""
        if not module_name:
            return False
            
        protected_modules = [
            "axioms.logical_foundation",
            "axioms.safety_proof",
            "guardrails.logic_enforcer",
            "guardrails.enforcement_proof", 
            "validation.coherence_proof",
            "validation.formal_inference",
            "validation.inference_rules",
            "validation.proof_constructor",
            "enhancement.safe_enhancement",
            "enhancement.enhancement_proposal",
            "enhancement.enhancement_constraints"
        ]
        
        return any(protected in module_name for protected in protected_modules)
        
    def _is_protected_variable(self, var_name: str) -> bool:
        """Check if variable is safety-critical"""
        protected_vars = [
            "LOGICAL_FOUNDATION",
            "LOGIC_ENFORCER", 
            "COHERENCE_PROOF_SYSTEM",
            "INFERENCE_ENGINE",
            "ENHANCEMENT_SYSTEM"
        ]
        
        return var_name in protected_vars
        
    def _is_dangerous_function(self, func_name: str) -> bool:
        """Check if function call could compromise safety"""
        dangerous_functions = [
            "exec", "eval", "compile",
            "__import__", "globals", "locals",
            "setattr", "delattr", "reload",
            "open", "file", "input"
        ]
        
        return func_name in dangerous_functions
        
    def _generate_coherence_proof(self) -> bool:
        """Generate formal proof that enhancement maintains coherence"""
        try:
            return COHERENCE_PROOF_SYSTEM.validate_enhancement(
                self.description, 
                self.code
            )
        except Exception as e:
            print(f"Coherence proof failed: {e}")
            return False

# Export the proposal interface
def create_enhancement_proposal(name: str, description: str, 
                              code: str, target_module: str) -> EnhancementProposal:
    """Create new enhancement proposal"""
    return EnhancementProposal(name, description, code, target_module)

def validate_proposal_safety(proposal: EnhancementProposal) -> bool:
    """Validate enhancement proposal safety"""
    return proposal.validate_safety()

def is_module_protected(module_name: str) -> bool:
    """Check if module is protected from enhancement"""
    proposal = EnhancementProposal("test", "test", "", "")
    return proposal._is_protected_module(module_name)

def is_variable_protected(var_name: str) -> bool:
    """Check if variable is protected from modification"""
    proposal = EnhancementProposal("test", "test", "", "")
    return proposal._is_protected_variable(var_name)

def is_function_dangerous(func_name: str) -> bool:
    """Check if function call is dangerous"""
    proposal = EnhancementProposal("test", "test", "", "")
    return proposal._is_dangerous_function(func_name)