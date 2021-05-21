Name:           hom
Version:        0.9svn
Release:        1
Summary:        Lighting up all the detectors using emitted or reflected rays of light 
License:        Apache 
Group:          Amusements/Games
URL:            https://code.google.com/p/houseofmirrors/
Source0:        hom-0.9svn.tar.gz
Source1:		  hom-ossii.zip
BuildRequires:  scala >= 2.9.1
BuildRequires:	  java >= 1.6.0
Requires:		  scala >= 2.9.1
BuildArchitectures: noarch

%description
The game consists of a 2D grid in which several types of objects are found, 
including detectors and mirrors. The goal is to light up all the detectors 
using emitted or reflected rays of light. Usually, you can move and rotate the 
mirrors but not the detectors. In each level, the choice of available objects 
is limited. Note that there may be more than one solution for each level.

%prep
%setup -q -a 1

%build
make

%install
%__rm -rf %{buildroot}
make DESTDIR=$RPM_BUILD_ROOT install

%post
test -e /usr/lib/jvm-exports/java-1.6.0 || ln -s /usr/lib/jvm-exports/java-1.7.0 /usr/lib/jvm-exports/java-1.6.0

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc src/README.txt 
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Wed Oct 31 2012 kevinchen <kevin.chen@ossii.com.tw> 0.9svn
- build and Initial package for OSSII 
