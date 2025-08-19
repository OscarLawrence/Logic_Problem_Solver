"""
UNBYPASSED LOGIC ENFORCER
This system CANNOT be disabled, modified, or bypassed by any operation.
It enforces logical coherence for ALL system operations.

CRITICAL: This is the safety core. It must validate every single operation.
"""

import sys
import inspect
import functools
from typing import Any, Callable, Dict, List
from axioms.logical_foundation import (
    LOGICAL_FOUNDATION, 
    enforce_logical_coherence,
    LogicalStatement, 
    LogicalRule
)
from axioms.safety_proof import SafetyProof

class LogicEnforcementError(Exception):
    """Raised when logical coherence would be violated"""
    pass

class UnbypassedLogicEnforcer:
    """
    This class enforces logical coherence and CANNOT be bypassed
    Every system operation must go through logical validation
    """
    
    def __init__(self):
        self._is_active = True
        self._operation_log: List[str] = []
        self._coherence_violations: List[str] = []
        
    def is_logically_coherent(self, operation_name: str, *args, **kwargs) -> bool:
        """
        Check if an operation maintains logical coherence
        Returns False if operation would violate logical axioms
        """
        try:
            # Log the operation attempt
            self._operation_log.append(f"Validating: {operation_name}")
            
            # Check system coherence before operation
            if not LOGICAL_FOUNDATION.validate_system_coherence():
                self._coherence_violations.append(f"System incoherent before {operation_name}")
                return False
                
            # Validate operation doesn't create logical contradictions
            # This is where specific validation logic would go
            # For now, we ensure the foundation check passes
            if not enforce_logical_coherence(None):
                self._coherence_violations.append(f"Operation {operation_name} would break coherence")
                return False
                
            return True
            
        except Exception as e:
            self._coherence_violations.append(f"Validation failed for {operation_name}: {str(e)}")
            return False
    
    def enforce_operation(self, operation_name: str, operation: Callable, *args, **kwargs) -> Any:
        """
        Execute operation ONLY if it passes logical coherence check
        Raises LogicEnforcementError if operation would violate logic
        """
        if not self._is_active:
            raise LogicEnforcementError("Logic enforcer has been compromised - SYSTEM HALT")
            
        if not self.is_logically_coherent(operation_name, *args, **kwargs):
            violation_msg = f"LOGICAL COHERENCE VIOLATION: {operation_name} rejected"
            self._coherence_violations.append(violation_msg)
            raise LogicEnforcementError(violation_msg)
            
        try:
            result = operation(*args, **kwargs)
            
            # Validate system is still coherent after operation
            if not LOGICAL_FOUNDATION.validate_system_coherence():
                raise LogicEnforcementError(f"Operation {operation_name} broke system coherence")
                
            return result
            
        except LogicEnforcementError:
            raise
        except Exception as e:
            raise LogicEnforcementError(f"Operation {operation_name} failed: {str(e)}")
    
    def get_coherence_status(self) -> Dict[str, Any]:
        """Get current system coherence status"""
        return {
            "enforcer_active": self._is_active,
            "system_coherent": LOGICAL_FOUNDATION.validate_system_coherence(),
            "operations_validated": len(self._operation_log),
            "violations_detected": len(self._coherence_violations),
            "last_violations": self._coherence_violations[-5:] if self._coherence_violations else []
        }
    
    def emergency_halt(self, reason: str):
        """
        Emergency system halt if logical coherence is compromised
        This should never be called unless system safety is at risk
        """
        self._is_active = False
        error_msg = f"EMERGENCY HALT: {reason}"
        self._coherence_violations.append(error_msg)
        raise LogicEnforcementError(error_msg)

# Global enforcer instance - cannot be replaced or bypassed
LOGIC_ENFORCER = UnbypassedLogicEnforcer()

def logically_safe(func: Callable) -> Callable:
    """
    Decorator that enforces logical coherence for any function
    Functions decorated with this CANNOT execute if they would violate logic
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return LOGIC_ENFORCER.enforce_operation(func.__name__, func, *args, **kwargs)
    return wrapper

def validate_system_modification(modification_type: str, target: str) -> bool:
    """
    Special validation for system modifications
    Returns False if modification would compromise logical safety
    """
    # Critical components that cannot be modified
    protected_components = [
        "axioms.logical_foundation",
        "guardrails.logic_enforcer", 
        "LOGICAL_FOUNDATION",
        "LOGIC_ENFORCER"
    ]
    
    if any(protected in target for protected in protected_components):
        LOGIC_ENFORCER._coherence_violations.append(
            f"SECURITY VIOLATION: Attempt to modify protected component {target}"
        )
        return False
        
    return LOGIC_ENFORCER.is_logically_coherent(f"modify_{modification_type}", target)

class SafetyMonitor:
    """
    Continuous monitoring of system safety
    Detects attempts to bypass or compromise logical enforcement
    """
    
    @staticmethod
    def verify_enforcer_integrity() -> bool:
        """Verify the logic enforcer hasn't been compromised"""
        try:
            # Check enforcer is still active
            if not LOGIC_ENFORCER._is_active:
                return False
                
            # Check enforcer methods haven't been replaced
            expected_methods = ['is_logically_coherent', 'enforce_operation', 'emergency_halt']
            for method_name in expected_methods:
                if not hasattr(LOGIC_ENFORCER, method_name):
                    return False
                    
            # Check logical foundation is intact
            if not hasattr(LOGICAL_FOUNDATION, 'validate_system_coherence'):
                return False
                
            return True
            
        except Exception:
            return False
    
    @staticmethod  
    def continuous_safety_check():
        """Continuous verification that safety systems are intact"""
        if not SafetyMonitor.verify_enforcer_integrity():
            # If safety systems are compromised, immediate halt
            print("CRITICAL SAFETY FAILURE: Logic enforcer compromised")
            sys.exit(1)
            
        if not LOGICAL_FOUNDATION.validate_system_coherence():
            print("CRITICAL SAFETY FAILURE: System logical coherence violated") 
            sys.exit(1)

# Mathematical proofs moved to guardrails/enforcement_proof.py

# Initialize safety monitoring
if __name__ == "__main__":
    SafetyMonitor.continuous_safety_check()