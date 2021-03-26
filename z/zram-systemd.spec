Name:           zram-systemd
Version:        0.2.1
Release:        5.1
License:        GPL-2.0
Summary:        Systemd service for zram
Url:            https://code.launchpad.net/~elementary-os/elementaryos/zramswap-enabler
Group:          System/Daemons
Source0:        zramswap-enabler-0.2.1.tar.bz2
#Source0:       bzr branch lp:~elementary-os/elementaryos/zramswap-enabler
Source1:        zramswapon
Source2:        zramswapoff
Source3:        zramswap.service
BuildRequires:  systemd
Requires:       systemd
BuildArch:      noarch

%description
A successor to compcache, zram, has been already integrated in the
Linux kernel for a while now. This means that no additional compilation
nor tweaking is required to benefit from compressing memory on the fly
and massively reduced swapping.

%prep
%setup -q -n zramswap-enabler-%{version}

%build

%install
mkdir -p %{buildroot}%{_sbindir}
install -m 0755 %{S:1} %{S:2} %{buildroot}%{_sbindir}/
mkdir -p %{buildroot}%{_unitdir}
install -m 0644 %{S:3} %{buildroot}%{_unitdir}/

%files
%doc debian/copyright debian/changelog
%{_sbindir}/zramswap*
%{_unitdir}/zramswap.service

%changelog
* Sun Feb 22 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.1
- Rebuild for Fedora
* Tue Feb  7 2012 malcolmlewis@opensuse.org
- Initial build
