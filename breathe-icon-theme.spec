%define theme_name Breathe

Summary: %{theme_name} icon theme
Name: breathe-icon-theme
Version: 0.51
Release: 4.1
License: Creative Commons - Attribution Share Alike
Group: User Interface/Desktops
URL: https://launchpad.net/breathe-icon-set
Source: https://launchpadlibrarian.net/33006992/%{name}-%{version}.tar.gz
BuildArch: noarch

%description
Because humans need oxygen.
A new effort to create a set of icons mixing the modern style of KDEs "Oxygen"
icons with Ubuntu's "Human" set.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/icons/%{theme_name}

%changelog
* Wed Jul 04 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.51
- Rebuild for Fedora
