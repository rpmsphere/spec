%define __os_install_post %{nil}

Name:		smake
Version:	1.2.5
Release:	5.1
Summary:	The Schily Make Program
Source:		ftp://ftp.berlios.de/pub/%{name}/%{name}-%{version}.tar.bz2
Group:		Development/Tools/Building
License:	GNU General Public License (GPL)
BuildRequires:	make gcc glibc-devel

%description
Smake is the only make program with automake features, it is the only program
that works on unknown platforms..

Smake executes command sequences based on relations of modification dates of
files. The command sequences are taken from a set of rules found in a makefile
or in the set of implicit rules. The argument target is typically a program
that is to be built from the known rules.

If no -f option is present, smake looks for SMakefile then for Makefile and
then for makefile in the named order.

If no target is specified on the command line, smake uses the first target that
could be found in makefilename and that does not start with a dot ('.').

If a target has no explicit entry in the makefile smake tries to use implicit
rules or the .DEFAULT rule.

Unlike most other make programs, smake propagates all com­ mand line macros to
sub makes. This is a big advantage with hierarchical makefile systems.
Propagation is done in a POSIX compliant way using the MAKEFLAGS= environment.

Unlike other make programs, smake includes a set of automake features that
allow to implement portable, layered, object oriented makefiles.

Authors:
--------
    Joerg Schilling <schilling@fokus.gmd.de>

%prep
%setup -q

%build
%__make %{?jobs:-j%{jobs}} CWARNOPTS="%{optflags}"

%install
make install DESTDIR=$RPM_BUILD_ROOT INS_BASE=/usr MANDIR=man
%__rm -f $RPM_BUILD_ROOT/usr/lib/*.a $RPM_BUILD_ROOT/usr/lib/profiled/*.a

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%doc AN-%{version} PORTING README* smake/defaults.smk
%{_bindir}/smake
%config(noreplace) /usr/lib/defaults.smk
%{_includedir}/schily
%{_mandir}/man1/smake.1*
%{_mandir}/man5/make*.5*

%changelog
* Fri Aug 07 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.5
- Rebuild for Fedora
* Tue Mar 25 2008 Pascal Bleser <guru@unixtech.be> 1.2a41
- new package
