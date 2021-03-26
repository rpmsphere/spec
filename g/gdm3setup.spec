Name: gdm3setup
Summary: An interface to configure GDM3
Version: 20140316
Release: 2.1
Group: GNOME desktop
License: GPL
URL: http://github.com/Nano77/gdm3setup
Source0: %{name}-master.zip
BuildArch: noarch
BuildRequires: desktop-file-utils
Requires: gdm

%description
An interface to configure GDM3, autologin options and change Shell theme.

%prep
%setup -q -n %{name}-master

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/locale

%changelog
* Wed May 25 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 20140316
- Rebuild for Fedora
