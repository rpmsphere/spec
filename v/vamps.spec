%undefine _debugsource_packages

Name:          vamps
Version:       0.99.2
Release:       3.1
Summary:       DVD9 to DVD5 Backup Utility
Group:         Graphical Desktop/Applications/Utilities
URL:           https://vamps.sourceforge.net/
Source:        https://www.mirrorservice.org/sites/download.sourceforge.net/pub/sourceforge/v/va/%{name}/%{name}-%{version}.tar.gz
License:       GPL
BuildRequires: libdvdread-devel

%description
Vamps allow the copy of one or more titles from a DVD9 to a DVD5.

%prep
%setup -q

%build
make

%install
rm -rf "$RPM_BUILD_ROOT"
install -D -m 755 vamps/vamps $RPM_BUILD_ROOT%{_bindir}/vamps
install -D -m 755 play_cell/play_cell $RPM_BUILD_ROOT%{_bindir}/play_cell

%files 
%{_bindir}/vamps
%{_bindir}/play_cell

%clean
rm -rf "$RPM_BUILD_ROOT"

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.99.2
- Rebuilt for Fedora
* Tue May 27 2008 Silvan Calarco <silvan.calarco@mambasoft.it> 0.99.2-1mamba
- update to 0.99.2
* Wed May 07 2008 Tiziana Ferro <tiziana.ferro@email.it> 0.99-1mamba
- update to 0.99
* Tue Jun 14 2005  Alessandro Ramazzina <alessandro.ramazzina@qilinux.it> 0.97-1qilnx
- new version
* Wed May 18 2005  Matteo Bernasconi <voyagernm@virgilio.it> 0.94-1qilnx
- First Build
