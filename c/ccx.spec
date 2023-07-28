%undefine _debugsource_packages

Name:           ccx
Version:        2.20
Release:        1
Summary:        An open source finite element package
License:        GPL-2.0-only AND BSD-3-Clause AND SUSE-Public-Domain
Group:          Productivity/Scientific/Other
URL:            http://www.dhondt.de/
Source0:        http://www.dhondt.de/ccx_%{version}.src.tar.bz2
Source1:        http://www.dhondt.de/ccx_%{version}.test.tar.bz2
Source2:        ccx-rpmlintrc
# PATCH-FIX-OPENSUSE -- pass global optflags
Patch0:         ccx-2.16-build.patch
Patch1:         0001-Fixup-spooles-include-dir.patch
Patch2:         ccx-2.16-abaqus-shell-heat-transfer-elements-read.patch
Patch3:         0001-Add-missing-argument-for-inputerror-function-call.patch
Patch4:         0001-Use-interface-for-cubtri-callback-function.patch
BuildRequires:  arpack-devel
BuildRequires:  fdupes
BuildRequires:  gcc-fortran
BuildRequires:  lapack-devel
BuildRequires:  sed
BuildRequires:  spooles-devel

%description
CalculiX is a package designed to solve field problems.
The method used is the finite element method. So far only
structural problems can be solved but it is planned to
extend the capabilities.

%package examples
Summary:        Example problems for CalculiX
Group:          Productivity/Scientific/Other
BuildArch:      noarch
Conflicts:      ccx-doc < 2.16
Provides:       ccx-doc:%{_datadir}/%{name}-examples-2.12/achtel2.inp

%description examples
CalculiX is a package designed to solve field problems.
The method used is the finite element method. %{name}-examples
contains examples problems, together with reference data
to check your installation.

%prep
%setup -c -q
%setup -D -T -a 1 -q
# fixup dirs: very deep directory structure, not suitable for patching
mv CalculiX/ccx_%{version}/{src,test} ./
rmdir -p CalculiX/ccx_%{version}
#autopatch -p1
#patch0 -p1
#patch1 -p1
#patch2 -p1
#patch3 -p1
%patch4 -p1

# Make reproducible
sed -i 's@./date.pl; *@@' src/Makefile

sed -i -e '21,26d' -e '27i LIBS = -lpthread -lm -lc -lspooles -larpack -lflexiblas' src/Makefile
sed -i -e 's|misc.h|spooles/misc/misc.h|' -e 's|FrontMtx.h|spooles/FrontMtx/FrontMtx.h|' -e 's|SymbFac.h|spooles/SymbFac/SymbFac.h|' src/spooles.h src/cascade.c

%build
cd src
export CFLAGS="%{optflags}"
export FFLAGS="%{optflags}"
%make_build

%install
mkdir -p %{buildroot}/%{_bindir}
cp src/ccx_%{version} %{buildroot}/%{_bindir}
chmod 755 %{buildroot}/%{_bindir}/ccx_%{version}
# symlink needed or apps like FreeCAD won't find it
ln -s ccx_%{version} %{buildroot}/%{_bindir}/ccx

mkdir -p %{buildroot}/%{_datadir}/%{name}-examples-%{version}
cp test/* %{buildroot}/%{_datadir}/%{name}-examples-%{version}
chmod 644 %{buildroot}/%{_datadir}/%{name}-examples-%{version}/*
chmod 755 %{buildroot}/%{_datadir}/%{name}-examples-%{version}/compare
chmod 755 %{buildroot}/%{_datadir}/%{name}-examples-%{version}/datcheck.pl
chmod 755 %{buildroot}/%{_datadir}/%{name}-examples-%{version}/frdcheck.pl
chmod 755 %{buildroot}/%{_datadir}/%{name}-examples-%{version}/compare_valgrind_leaks

chmod 444 src/BUGS src/LOGBOOK src/README.INSTALL src/TODO

%fdupes %{buildroot}/%{_datadir}/%{name}-examples-%{version}

%check
cd test
# beamread* depends on beamwrite*
# beamprand is random
# beamptied{5,6} have nondeterministic order of eigenvalues
for f in beamread*.inp beamprand.inp beamptied{5,6}.inp ; do mv $f ${f}_disabled ; done
set +x
for input in beam*.inp ; do
    f=`basename $input .inp`
    echo -n "Procesing $f "
    %{buildroot}/%{_bindir}/ccx $f >> ccxlog || echo -n "-> $?" ; echo
    [ -f $f.dat -a -f $f.frd ] || echo "$f failed!" | tee -a errorlog
    [ "$(wc -l < $f.dat)" -eq "$(wc -l < $f.dat.ref)" ] || echo "Wrong size: $f.dat" | tee -a errorlog
    grep NaN $f.dat && echo "Contains NaN: $f.dat" | tee -a errorlog
    ./datcheck.pl $f | tee -a errorlog
    [ -f $f.frd.ref ] || continue
    [ "$(wc -l < $f.frd)" -eq "$(wc -l < $f.frd.ref)" ] || echo "Wrong size: $f.frd" | tee -a errorlog
    ./frdcheck.pl $f | tee -a errorlog
done
set -x
if [ -s errorlog ] ; then
    cat ccxlog
    cat errorlog
#    exit 1
fi

%files
%{_bindir}/ccx
%{_bindir}/ccx_%{version}
%doc src/BUGS src/LOGBOOK src/README.INSTALL src/TODO

%files examples
%{_datadir}/%{name}-examples-%{version}

%changelog
* Sun Jul 02 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 2.20
- Rebuilt for Fedora
* Tue Feb 23 2021 Stefan Brüns <stefan.bruens@rwth-aachen.de>
- update to 2.17:
  Too many changes to list, a full list of changes is
  available in the included LOGFILE.
- Rebase patches, renamed ccx-2.16-spooles-dynamic.patch
  - > 0001-Fixup-spooles-include-dir.patch
- Add 0001-Add-missing-argument-for-inputerror-function-call.patch
- Add 0001-Use-interface-for-cubtri-callback-function.patch
- Enable check section
* Thu Nov 28 2019 Stefan Brüns <stefan.bruens@rwth-aachen.de>
- update to 2.16:
  Too many changes to list, a full list of changes is
  available in the included LOGFILE.
  (boo#1146243).
- Examples/tests are now packages in the ccx-examples package
- Move docs to separate source package
- Update patches:
  * Drop (not applied) ccx-2.8-no-local-compare.patch
  * Drop ccx-1.2-doc-Makefile.patch
  * ccx-2.8-build.patch -> ccx-2.16-build.patch, foo.patch
  * ccx-2.5-abaqus-shell-heat-transfer-elements-read.patch ->
    ccx-2.16-abaqus-shell-heat-transfer-elements-read.patch
  * ccx-2.8-spooles-dynamic.patch -> ccx-2.16-spooles-dynamic.patch
* Wed Jul 19 2017 adrian@suse.de
- update to 2.12
* Sun May 31 2015 avvissu@yandex.ru
- Update to 2.8p2:
- Procedures:
  * computational Fluid Dynamics based on finite volumes works for
    laminar incompressible flow
  * for frequency calculations participation factors and relative
    effective modal masses are calculated and stored in the .dat
  * rayleigh damping (*DAMPING), contact damping and dashpots were
    implemented for nonlinear dynamic calculations (*DYNAMIC)
  * magnetostatic and inductive heating calculations are available
    with the *ELECTROMAGNETICS keyword
  * surfaces tied by cyclic symmetry conditions can now also be
    face-based
  * stiffness of a substructure (= superelement) can be calculated
    and stored using the *SUBSTRUCTURE GENERATE and *SUBSTRUCTURE
    MATRIX OUTPUT cards
- Elements:
  * beams with a pipe section were implemented (= square cross
    section with special integration scheme)
  * replaced the expandable rigid bodies by mean rotations MPC's
    for the app of rotations and/or moments to beams and shells
- Materials:
  * a linear elastoplastic material was implemented (additive
    decomposition of the total strain)
  * a Ciarlet type elastic model for large deformations was
    implemented
  * a single crystal creep model was implemented
- Output:
  * the text underneath *HEADING is stored in the frd-file
  * POT, ECD, EMFE and EMFB labels for the output of the electric
    potential, electric current density, electric field and
    magnetic field into the .frd-file
- Update patches:
  * ccx-2.6-build.patch -> ccx-2.8-build.patch
  * ccx-2.6-no-local-compare.patch -> ccx-2.8-no-local-compare.patch
  * ccx-2.0-spooles-dynamic.patch -> ccx-2.8-spooles-dynamic.patch
* Tue Oct 28 2014 avvissu@yandex.ru
- Fix build error on openSUSE > 12.3:
  * add BuildRequires: tex(pst-tools.tex)
* Thu Jul 11 2013 scorot@free.fr
- version 2.6
  * See https://www.dhondt.de/new_calc.htm for details
* Mon Mar 18 2013 scorot@free.fr
- fix latex requirements on 12.3 and Factory
* Tue Oct  9 2012 scorot@free.fr
- version 2.5
  * See https://www.dhondt.de/new_calc.htm for details
- spec file cleanup and reformating
- update patches
* Tue Jul  3 2012 scorot@free.fr
- add patch from Guido Dhondt to fix compiler warnings
* Thu Jun  7 2012 scorot@free.fr
- do not link against openblas since arpack is linked against
  reference blas and lapack
* Sun May  6 2012 scorot@free.fr
- spec file cleanup
* Wed Mar 21 2012 scorot@free.fr
- version 2.4
- fix documentation build on recent texlive
- change package group
- doc package is noarch for 11.3 and higher
* Fri Mar 16 2012 scorot@free.fr
- update patch0 to use openblas
* Mon Mar 12 2012 scorot@free.fr
- use arpack-ng instead of arpack
