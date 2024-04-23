Name:		praat
Summary:	Doing phonetics, speech analysis and synthesis by computer
Version:	6.4.07
Release:	1
License: 	GPLv2
Group:		Sciences/Other
URL:		https://www.fon.hum.uva.nl/praat/
BuildRequires:	libXp-devel
BuildRequires:	libXt-devel
BuildRequires:	libSM-devel
BuildRequires:	libICE-devel
BuildRequires:	libXext-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	libXmu-devel
BuildRequires:	motif-devel
BuildRequires:	gtk2-devel
BuildRequires:	cairo-devel
Source0:	https://codeload.github.com/praat/praat/tar.gz/refs/tags/v%{version}#/%{name}-%{version}.tar.gz
Source1:	praat.png
Source2:	praat.desktop

%description
According to its authors, praat is "doing phonetics by computer". There are
several speech analysis functionalities available: spectrograms, cochleograms,
and pitch and formant extraction. Articulatory synthesis, as well as synthesis
from pitch, formant, and intensity are also available. Other features are
segmentation, labelling using the phonetic alphabet, and computation of
statistics.

%prep
%setup -q
#sed -i 's|-lasound|-lasound -lpthread|' makefiles/makefile.defs.linux.alsa
#sed -i 's|-Wunused|-Wunused -Wno-narrowing -std=c++98|' makefiles/makefile.defs.linux.alsa

%build
cp makefiles/makefile.defs.linux.pulse makefile.defs
make

%clean
rm -rf %{buildroot}

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/applications
mkdir -p %{buildroot}/%{_datadir}/pixmaps

# the application itself
cp -vf ./praat %{buildroot}/usr/bin

# icons provided by antonino mingoia from www.ozzpot.com
cp -vf %{SOURCE1} %{buildroot}/%{_datadir}/pixmaps

# our own desktop entry
cp -vf %{SOURCE2} %{buildroot}/%{_datadir}/applications

%files
%doc README.md
%{_bindir}/praat
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop

%changelog
* Sun Apr 14 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 6.4.07
- Rebuilt for Fedora
* Wed Mar 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 5.2.17-1mdv2011.0
+ Revision: 645380
- update to new version 5.2.17
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 5.1.29-2mdv2011.0
+ Revision: 614609
- the mass rebuild of 2010.1 packages
* Thu Mar 11 2010 Caio Begotti <caio1982@mandriva.org> 5.1.29-1mdv2010.1
+ Revision: 518189
- new upstream version (changes from the standard lesstif/motif toolkit to gtk and cairo)
* Thu Jan 21 2010 Frederik Himpe <fhimpe@mandriva.org> 5.1.25-1mdv2010.1
+ Revision: 494656
- update to new version 5.1.25
* Mon Dec 21 2009 Caio Begotti <caio1982@mandriva.org> 5.1.22-1mdv2010.1
+ Revision: 480905
- new upstream version
* Wed Sep 16 2009 Caio Begotti <caio1982@mandriva.org> 5.1.15-1mdv2010.0
+ Revision: 443548
- new upstream version, fixes the hanging issue
- fix the categories used for praat
- fix the summary, it was not making much sense
* Thu May 21 2009 Frederik Himpe <fhimpe@mandriva.org> 5.1.7-1mdv2010.0
+ Revision: 378427
- update to new version 5.1.7
* Sun May 10 2009 Frederik Himpe <fhimpe@mandriva.org> 5.1.5-2mdv2010.0
+ Revision: 374049
- Really update to 5.1.5
- Add sed hack to convert version string in source version string with
  leading zero: should make mdvsys update work as expected
- Improve summary
* Sun May 10 2009 Frederik Himpe <fhimpe@mandriva.org> 5.1.5-1mdv2010.0
+ Revision: 374037
- update to new version 5.1.5
* Wed Apr 01 2009 Caio Begotti <caio1982@mandriva.org> 5.1.3-1mdv2009.1
+ Revision: 363330
- wrong package name dependency
- fix the menu entry, it's more a scientific app rather an education utility
- import praat
* Wed Apr 01 2009 Caio Begotti <caio@mandriva.com> 5.1.3-1mdv2009.1
- First version, initial import
