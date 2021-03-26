Name: amd-driver
Summary: Compatible package for fglrx
Version: 15.20.1046
Release: 1
License: Commercial, Freeware
URL: http://ati.amd.com/support/driver.html
Group: System/Kernel and hardware
Requires: redhat-lsb-core
%ifarch x86_64
Requires: fglrx64_p_i_c = %{version}
%else
Requires: fglrx_p_i_c = %{version}
%endif
Obsoletes: ocl-icd
Source1: 00-fglrx.conf

%description
This is the compatible meta-package for the AMD proprietary kernel module,
X.org driver and libraries.

%install
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/X11/xorg.conf.d/00-fglrx.conf

%files
%{_datadir}/X11/xorg.conf.d/00-fglrx.conf

%preun
aticonfig --uninstall || :

%post
/sbin/ldconfig
aticonfig --initial -f || :
rm -f /usr/share/applications/amdccclesu.desktop

%changelog
* Tue Sep 01 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 15.20.1046
- Initial package
