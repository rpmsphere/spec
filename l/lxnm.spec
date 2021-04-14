Name:           lxnm
Version:        0.2.2
Release:        1
Summary:        Network Manager for LXDE
Group:          Applications/System
License:        GPL
URL:            http://sourceforge.net/project/showfiles.php?group_id=180858
Source:         http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz

%description
LXNM is a fast, lightweight, stand-alone network manager.

%prep
%setup -q

%build
%configure
%__make %{?_smp_mflags}

%install
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%doc README AUTHORS COPYING
%{_sbindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.2
- Rebuilt for Fedora
