# 
# Do not Edit! Generated by:
# spectacle version 0.17
# 
# >> macros
# << macros

Name:       moblin-desktop-files
Summary:    Desktop files overlay
Version:    0.2.0
Release:    3.1
Group:      System/Desktop
License:    GPLv2
URL:        http://www.moblin.org
Source0:    %{name}-%{version}.tar.gz
Source100:  moblin-desktop-files.yaml
Patch0:     msgid-capitalization.patch
BuildRequires:  intltool
BuildRequires:  gettext


%description
Custom desktop files for MeeGo



%prep
%setup -q -n %{name}-%{version}

# msgid-capitalization.patch
%patch0 -p1
# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static
make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%makeinstall

# >> install post
# << install post
%find_lang moblin-desktop-files






%files -f moblin-desktop-files.lang
%defattr(-,root,root,-)
# >> files
%dir %{_datadir}/applications-meego
%{_datadir}/applications-meego/*.desktop
# << files

%clean
rm -rf %{buildroot}


%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuilt for Fedora
* Tue Oct 26 2010 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII
* Mon Jul 19 2010 awafaa@opensuse.org
- Initial import for openSUSE version 0.2.0
