%undefine _debugsource_packages
%define pyname ccc-gistemp

Name:           python-%{pyname}
Version:        0.6.1
Release:        21.1
Summary:        Clear Climate Code GISTEMP project
License:        BSD
URL:            https://code.google.com/p/ccc-gistemp/
Group:          Productivity/Scientific/Other
Source0:        %{pyname}-%{version}.tar.bz2
Source1:        ccc-gistemp.desktop
BuildArch:      noarch
BuildRequires:  python2
BuildRequires:  python2-setuptools
Requires:       numpy

%description
ccc-gistemp is a reimplementation of GISTEMP in Python for clarity. GISTEMP is
a reconstruction of the global historical temperature record from land and sea
surface temperature records. It produces a familiar graph of historical
temperatures.

%prep
%setup -q -n %{pyname}-%{version}

%build
python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT
#install the data
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/
mv $RPM_BUILD_ROOT%{_prefix}/CCF_48x48.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/ccf.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mv $RPM_BUILD_ROOT%{_prefix}/*.* $RPM_BUILD_ROOT%{_datadir}/%{name}
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/ccc-gistemp.desktop

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%files
%doc readme.txt release-notes.txt
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/ccc-gistemp.desktop
%{_datadir}/icons/hicolor/48x48/apps/ccf.png
%{python2_sitelib}/*

%changelog
* Wed Dec 28 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.1
- Rebuilt for Fedora
* Wed Jun  1 2011 ocefpaf@yahoo.com.br
- First release; version 0.6.1
