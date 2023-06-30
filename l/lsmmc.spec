Name:           lsmmc
Version:        20120621
Release:        1
Summary:        Userspace tools for MMC/SD storage devices
License:        BSD
Group:          Hardware/Other
URL:            https://comments.gmane.org/gmane.linux.kernel.mmc/15223
#Source0:        https://cache.gmane.org//gmane/linux/kernel/mmc/15223-001.bin
Source0:        %{name}.tar.gz
BuildRequires:  ctags

%description
lsmmc is created by Sebastian Rasmussen formerly at ST-Ericsson.
It contains an extensive parser of the CID, CSD, SCR and EXT_CSD
registers, as well as an archive of these registers for over 120
eMMC and SD-cards. The utility works as-is and uses sysfs to read
the register values. Usage: lsmmc -v /sys/block/mmcblk0/device

%prep
%setup -q -n %{name}

%build
make

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm644 %{name}.ids %{buildroot}%{_sysconfdir}/%{name}.ids

%files
%{_bindir}/%{name}
%{_sysconfdir}/%{name}.ids
%doc NOTICE

%changelog
* Tue May 12 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 20120621
- Initial package
