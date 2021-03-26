#define __arch_install_post %{nil}
#undefine _missing_build_ids_terminate_build
%global debug_package %{nil}
%global kversion %(uname -r)

Summary: 	Insyde SMBIOS Data Editor
Name: 		h2osde
Version: 	100.00.07.14
Release: 	1.bin
License: 	Commercial, freeware
Group:		Development/Tools
Source0:	InsydeH2OSDE_x86_LINUXx64_%{version}.zip
Source1:        InsydeH2OSDE_x86_LINUXx32_%{version}.zip
URL:		http://www.insyde.com/
BuildRequires:  kernel-headers
BuildRequires:  kernel-devel
Requires:	kernel = %(uname -r|sed 's/-.*//')

%description
Insyde SMBIOS Data Editor for Linux.

%prep
%ifarch x86_64
%setup -q -c
%else
%setup -q -c -T -a 1
%endif
sed -i '25i #include <linux/sched.h>' driver/phy_alloc.c

%build
cd driver
make phy_alloc

%install
mkdir -p %{buildroot}/usr/lib/insyde
cp h2osde-lx64 %{buildroot}/usr/lib/insyde
mkdir -p %{buildroot}/usr/lib/insyde/driver
cp driver/*.ko %{buildroot}/usr/lib/insyde/driver
mkdir -p %{buildroot}%{_bindir}
%ifarch x86_64
ln -s ../lib/insyde/h2osde-lx64 %{buildroot}%{_bindir}/%{name}
%else
ln -s ../lib/insyde/h2osde-l %{buildroot}%{_bindir}/%{name}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
/usr/lib/insyde/h2osde-l*
/usr/lib/insyde/driver/phy_alloc.ko

%changelog
* Wed Dec 06 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 100.00.07.14
- Initial package
