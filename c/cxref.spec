Name:           cxref
Version:    	1.6e
Release:    	5.1
Summary:    	C Cross Referencing & Documenting tool
Group:      	Development/Tools/Building
License:    	GPL-2.0
URL:        	https://www.gedanken.org.uk/software/cxref/
Source0:     	https://www.gedanken.org.uk/software/cxref/download/%{name}-%{version}.tgz
BuildRequires:  bison flex xz
BuildRequires:  automake autoconf libtool

%description  
Cxref is a program that will produce documentation (in LaTeX, HTML, RTF or SGML)
including cross-references from C program source code.

Works for ANSI C, including most gcc extensions.

The documentation for the program is produced from comments in the code that
are appropriately formatted. The cross referencing comes from the code itself
and requires no extra work.

The documentation is produced for each of the following:

Files            - A comment that applies to the whole file.
Functions        - A comment for the function, including a description of
                   each of the arguments and the return value.
Variables        - A comment for each of a group of variables and/or
                   individual variables.
#include         - A comment for each included file.
#define          - A comment for each pre-processor symbol definition, and
                   for macro arguments.
Type definitions - A comment for each defined type and for each element of a
                   structure or union type.

Any or all of these comments can be present in suitable places in the
source code.


The cross referencing is performed for the following items

Files           - The files that the current file is included in
                  (even when included via other files).

#includes       - Files included in the current file.
                - Files included by these files etc.

Variables       - The location of the definition of external variables.
                - The files that have visibility of global variables.
                - The files / functions that use the variable.

Functions       - The file that the function is prototyped in.
                - The functions that the function calls.
                - The functions that call the function.
                - The files and functions that reference the function.
                - The variables that are used in the function.

Each of these items is cross referenced in the output.

Includes extensive README and FAQ with details and examples on how to use the
program.

%prep  
%setup -q

%build  
#autoreconf -fi
%configure
make
#make docs
  
%install  
%makeinstall
install -m 755 contrib/knr2ansi.pl $RPM_BUILD_ROOT%{_bindir}/knr2ansi

%files
%{_bindir}/*
%{_datadir}/%{name}-cpp.defines
%{_mandir}/man1/*.1.gz

%changelog
* Tue Feb 27 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6e
- Rebuilt for Fedora
* Fri Jul  6 2012 pth@suse.de
- Update to 1.6d:
  Bug fixes
    Updated for latest version of autoconf.
    Allow structure initialisers to have multiple components
    (e.g. a.b=1).
    Remove gcc warning messages.
    Change Makefile for better comptibility with FreeBSD.
- Explicit require automake, autoconf and libtool.
- Repackage as tar.xz.
* Tue Jan 11 2011 pth@novell.com
- Initial package
