# Cyber-investigation Analysis Standard Expression (CASE)

_Read the [CASE Wiki tab](https://github.com/casework/CASE/wiki) to learn **everything** you need to know about the Cyber-investigation Analysis Standard Expression (CASE) ontology._
_For learning about the Unified Cyber Ontology, CASE's parent, see [UCO](https://github.com/ucoProject/UCO)._

# Proof-of-Concept CASE Volatility Plugins

_**Note: This POC is not ontology-correct!**_

This repository contains a sub-set of [Volatility](https://github.com/volatilityfoundation/volatility/)
plugins that produce output in the [CASE](https://github.com/casework/CASE) format.

These plugins have been taken from core Volatility plugins and adapted
the output to produce CASE JSON-LD. These currently are **proof-of-concept
only**, and may not fully comply to the CASE ontology as it is an evolving standard.

This repository takes the following plugins from the [Volatility framework](https://github.com/volatilityfoundation/volatility/)
and adapats the output to be CASE compliant based on the v0.1.0 release:

* [handles.py](https://github.com/volatilityfoundation/volatility/blob/master/volatility/plugins/handles.py)
* [procdump.py](https://github.com/volatilityfoundation/volatility/blob/master/volatility/plugins/procdump.py)
* [cmdline.py](https://github.com/volatilityfoundation/volatility/blob/master/volatility/plugins/cmdline.py)


All [Volatility](https://github.com/volatilityfoundation/volatility/) work belongs to their respective authors which can be found [here](https://github.com/volatilityfoundation/volatility/blob/master/AUTHORS.txt).


### Installation  of 3rd Party Libraries
* [CASE Python Library](https://github.com/casework/CASE-Python-API).
* [Volatility Python library](https://github.com/volatilityfoundation/volatility/wiki/Installation).


### Running Custom PoC Plugins


CASE Handle List from Memory Image:
```
vol.py --plugins='volplugs/src/' -f memory_images/memory.img --profile WinXPSP2x86 casehandles
```

CASE Procdump:
```
vol.py --plugins='volplugs/src/' -f memory_images/memory.img caseprocdump --dump-dir dumpdir
```

CASE Commandline dumping:
```
vol.py --plugins='volplugs/src/' -f memory_images/memory.img casecmdline
```

# I have a question!

Before you post a Github issue or send an email ensure you've done this checklist:

1. [Determined scope](https://caseontology.org/ontology/start.html#scope) of your task. It is not necessary for most parties to understand all aspects of the ontology, mapping methods, and supporting tools.

2. Familiarize yourself with the [labels](https://github.com/casework/CASE-Implementation-Volatility/labels) and search the [Issues tab](https://github.com/casework/CASE-Implementation-Volatility/issues). Typically, only light-blue and red labels should be used by non-admin Github users while the others should be used by CASE Github admins.
*All but the red `Project` labels are found in every [`casework`](https://github.com/casework) repository.*
