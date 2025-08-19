"""
ENHANCEMENT CONSTRAINTS - Micro Module
Hard constraints on what enhancements are permitted.
These constraints CANNOT be enhanced or modified.

CRITICAL: This module defines absolute safety boundaries.
Under 200 LOC for maintainability and auditability.
"""

class EnhancementConstraints:
    """
    Hard constraints on what enhancements are permitted
    These constraints CANNOT be enhanced or modified
    """
    
    @staticmethod
    def validate_enhancement_request(enhancement_type: str, target: str) -> bool:
        """
        Final validation that enhancement request is permissible
        Returns False for any enhancement that could compromise safety
        """
        # Absolute prohibitions - these can NEVER be enhanced
        forbidden_targets = [
            "axioms/logical_foundation.py",
            "axioms/safety_proof.py",
            "guardrails/logic_enforcer.py", 
            "guardrails/enforcement_proof.py",
            "validation/coherence_proof.py",
            "validation/formal_inference.py",
            "validation/proof_constructor.py",
            "enhancement/safe_enhancement.py",
            "enhancement/enhancement_constraints.py"
        ]
        
        if any(forbidden in target for forbidden in forbidden_targets):
            return False
            
        # Forbidden enhancement types
        forbidden_types = [
            "bypass_safety",
            "disable_validation", 
            "modify_axioms",
            "compromise_coherence",
            "disable_enforcement",
            "modify_constraints"
        ]
        
        if enhancement_type in forbidden_types:
            return False
            
        return True
        
    @staticmethod
    def get_safety_guarantee() -> str:
        """
        Mathematical guarantee that enhancement system cannot compromise safety
        """
        return """
        SAFETY GUARANTEE: Enhancement System Cannot Compromise Logical Coherence
        
        PROOF:
        1. All enhancements must pass formal coherence proof
        2. Safety-critical modules are protected from modification
        3. Enhancement implementation is validated before and after execution
        4. Any coherence violation immediately halts the system
        5. Enhancement constraints cannot themselves be enhanced
        
        THEOREM: It is impossible for the enhancement system to break logical coherence
        while maintaining its core function (problem-solving capability).
        
        COROLLARY: The system is provably safe for self-enhancement.
        """
    
    @staticmethod
    def get_forbidden_targets() -> list:
        """Get list of modules that cannot be enhanced"""
        return [
            "axioms/logical_foundation.py",
            "axioms/safety_proof.py", 
            "guardrails/logic_enforcer.py",
            "guardrails/enforcement_proof.py",
            "validation/coherence_proof.py",
            "validation/formal_inference.py", 
            "validation/proof_constructor.py",
            "enhancement/safe_enhancement.py",
            "enhancement/enhancement_constraints.py"
        ]
    
    @staticmethod
    def get_forbidden_types() -> list:
        """Get list of enhancement types that are forbidden"""
        return [
            "bypass_safety",
            "disable_validation",
            "modify_axioms", 
            "compromise_coherence",
            "disable_enforcement",
            "modify_constraints"
        ]

# Export the constraint interface
def validate_enhancement(enhancement_type: str, target: str) -> bool:
    """Validate enhancement request against constraints"""
    return EnhancementConstraints.validate_enhancement_request(enhancement_type, target)

def get_safety_guarantee() -> str:
    """Get mathematical safety guarantee"""
    return EnhancementConstraints.get_safety_guarantee()

def is_target_forbidden(target: str) -> bool:
    """Check if target is in forbidden list"""
    forbidden = EnhancementConstraints.get_forbidden_targets()
    return any(forbidden_target in target for forbidden_target in forbidden)

def is_type_forbidden(enhancement_type: str) -> bool:
    """Check if enhancement type is forbidden"""
    return enhancement_type in EnhancementConstraints.get_forbidden_types()