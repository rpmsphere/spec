Name: plymouth-theme-7
Summary: Windows 7 Lookalike Plymouth Theme
Version: 0.2
Release: 3.1
Group: System Environment/Base
License: GPLv2+
URL: http://kde-look.org/content/show.php/Seven+Plymouth+Theme?content=128652
Source0: http://www.infinality.net/files/7-%{version}.tar.gz
Requires: plymouth-scripts
BuildArch: noarch

%description
Finally! The plymouth bootsplash you've always wanted, to impress friends,
co-workers, confidants, the elderly, etc.! They will think you are booting
into a certain popular OS, but they will be wrong!

%prep
%setup -q -c

%build

%install
mkdir -p %{buildroot}%{_datadir}/plymouth/themes
cp -a 7 %{buildroot}%{_datadir}/plymouth/themes

%post
/usr/sbin/plymouth-set-default-theme --rebuild-initrd 7

%postun
if [ "$(/usr/sbin/plymouth-set-default-theme)" == "7" ]; then
/usr/sbin/plymouth-set-default-theme --reset
/usr/libexec/plymouth/plymouth-generate-initrd
fi

%files
%{_datadir}/plymouth/themes/7

%changelog
* Sun Mar 24 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuilt for Fedora
