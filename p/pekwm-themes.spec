Name:           pekwm-themes
Version:        1.0.5
Release:        13.1
License:        GPL
Group:          System/GUI/Other
Requires:       pekwm
URL:            https://adrinux.wordpress.com/pekwm-themes
Source:         %{name}-%{version}.tar.bz2
Summary:        PekWM themes by Adriano
BuildArch:	    noarch

%description
Several themes for PekWM windows manager by Adriano with ports of well known
interfaces.

%prep
%setup -q -n %{name}

%build

%install
mkdir -p %{buildroot}%{_datadir}/pekwm/themes
cp -r * %{buildroot}%{_datadir}/pekwm/themes
chmod -x %{buildroot}/usr/share/pekwm/themes/tango/*

%clean
%{__rm} -rf %{buildroot}

%files
%{_datadir}/pekwm/themes/*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.5
- Rebuilt for Fedora
* Sat Sep 26 2009 mhrusecky@suse.cz
- update - version 1.0.5
  - new blue and brown themes
* Tue Feb 10 2009 mhrusecky@suse.cz
- update - version 1.0.4
- License is now known - GPL
* Thu Dec 18 2008 mhrusecky@suse.cz
- initial package - version 1.0.3
