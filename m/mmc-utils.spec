Name:           mmc-utils
Version:        20191004
Release:        1
Summary:        Tools for MMC/SD devices
License:        GPL-2.0
Group:          Hardware/Other
URL:            https://git.kernel.org/cgit/linux/kernel/git/cjb/mmc-utils.git/
Source0:        %{name}-master.tar.gz
Source1:        https://www.gnu.org/licenses/gpl-2.0.txt

%description
Userspace tools for controlling and querying MMC/SD storage devices.

%prep
%setup -q -n %{name}-master
cp %{SOURCE1} LICENSE.GPL-2.0
sed -i 's|-Werror||' Makefile

%build
make

%install
%make_install prefix=/usr
install -Dm644 man/mmc.1 %{buildroot}%{_mandir}/man1/mmc.1

%files
%{_bindir}/mmc
%doc LICENSE.GPL-2.0
%{_mandir}/man1/mmc.1.*

%changelog
* Sun Apr 04 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 20191004
- Rebuilt for Fedora
* Thu Dec 25 2014 mpluskal@suse.com
- Initial packaging of current git snapshot (20140812)
