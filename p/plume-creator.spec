Summary:        A project manager and rich text editor for writers
Name:           plume-creator
Version:        0.66.2
Release:        1
License:        GPLv3+
Group:          Publishing
URL:            https://www.plume-creator.eu/
Source0:        https://sourceforge.net/projects/plume-creator/files/0.6/%{name}-%{version}.tar.gz
BuildRequires:  qt4-devel
#BuildRequires: hunspell-devel

%description
With %{name}, organize your writing projects. Scenes, notes, characters,...
Rich Text editing, full screen editing and multiple projects supported.

%prep
%setup -q
sed -i 's|VERSION = .*|VERSION = %{version}|' %{name}.pro

%build
%qmake_qt4 %{name}.pro
make

%install
%define apps       %{_datadir}/applications
%define pixmaps    %{_datadir}/icons/hicolor/scalable/apps
%define locale     %{_datadir}/%{name}/locale
 
rm -rf %{buildroot}
 
mkdir -p %{buildroot}%{_bindir}/
cp -p %{name} %{buildroot}%{_bindir}/
 
mkdir -p %{buildroot}%{apps}
cp -p resources/unix/applications/%{name}.desktop %{buildroot}%{apps}

mkdir -p %{buildroot}%{pixmaps}
cp -rp resources/images/icons/hicolor/scalable/apps/* %{buildroot}%{pixmaps}
 
mkdir -p %{buildroot}%{locale}
cp -p translations/*.qm %{buildroot}%{locale}

%files
%{_bindir}/%{name}
%{apps}/%{name}.desktop
%{pixmaps}/*
%{locale}/*.qm

%changelog
* Fri Sep 11 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.66.2
- Rebuilt for Fedora
* Wed Oct 15 2014 umeabot <umeabot> 0.66.1-3.mga5
+ Revision: 743529
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 0.66.1-2.mga5
+ Revision: 687682
- Mageia 5 Mass Rebuild
* Sat Aug 09 2014 filipesaraiva <filipesaraiva> 0.66.1-1.mga5
+ Revision: 661294
- Patch to show plume-creator icon
* Sun Nov 17 2013 filipesaraiva <filipesaraiva> 0.66.1-1.mga4
+ Revision: 551687
- imported package plume-creator
