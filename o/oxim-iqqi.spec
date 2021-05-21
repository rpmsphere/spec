Summary: Open X Input Method's IQQI wrapper
Name: oxim-iqqi
Version: 0.1.0
Release: 5
License: CDDL and LGPLv2+
Group: System/Internationalization
Source0: %{name}.tar.gz
Autoreq: no
BuildRequires: oxim-devel qt4-devel intltool >= 0.35.0
Requires: oxim >= 1.5.4 iqqi >= 1.8-5

%description
This package includes the wrapper for OXIM(Open X Input Method).

%prep
%setup -q -n %{name}

%build
for lang in zy py en; do
    pushd $lang;
    qmake-qt4 default.pro;
    %{__make} %{?_smp_mflags};
    popd;
done

%install
%{__mkdir_p} $RPM_BUILD_ROOT%{_libdir}/oxim/modules
mv en/liben.so.1.0.0 $RPM_BUILD_ROOT%{_libdir}/oxim/modules/iqqien.so
mv zy/libzy.so.1.0.0 $RPM_BUILD_ROOT%{_libdir}/oxim/modules/iqqizy.so
mv py/libpy.so.1.0.0 $RPM_BUILD_ROOT%{_libdir}/oxim/modules/iqqipy.so
%{__mkdir_p} $RPM_BUILD_ROOT%{_libdir}/oxim/panels
cp panels/* $RPM_BUILD_ROOT%{_libdir}/oxim/panels
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} \;
#rm -rf $RPM_BUILD_ROOT

%post
%{__cat} > %{_sysconfdir}/oxim/panel.conf << EOF
VIRTUAL_KEYBOARD=iqqi
AUTO_DOCK=no
INPUT_METHOD=iqqizy
EOF

oxim-agent -r

%postun
oxim-agent -r

%clean 
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
#%doc AUTHORS TODO README COPYING INSTALL LGPL.LICENSE OPENSOLARIS.LICENSE
%{_libdir}/oxim/modules/iqqi*.so
%{_libdir}/oxim/panels/*
#%{_datadir}/locale/*/LC_MESSAGES/sunpinyin.mo

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuilt for Fedora
* Thu Oct 27 2011 Wind Win <yc.yan@ossii.com.tw> 0.1.0-5
- Bug fixed for en module: the ability of keypad ENTER.

* Wed Oct 19 2011 Wind Win <yc.yan@ossii.com.tw> 0.1.0-4
- Bug fixed.

* Tue Oct 18 2011 Wind Win <yc.yan@ossii.com.tw> 0.1.0-3
- Bug fixed.

* Fri Oct  7 2011 Wind Win <yc.yan@ossii.com.tw> 0.1.0-2
- Bug fixed.

* Thu Oct  6 2011 Wind Win <yc.yan@ossii.com.tw> 0.1.0-1
- Bug fixed.

* Mon Sep 19 2011 Wind Win <yc.yan@ossii.com.tw> 0.0.4-2
- Bug fixed.

* Thu Sep 15 2011 Wind Win <yc.yan@ossii.com.tw> 0.0.4-1
- Bug fixed.

* Fri Aug 15 2011 Wind Win <yc.yan@ossii.com.tw> 0.0.3-6
- update file: iqqi.conf

* Fri Aug 12 2011 Wind Win <yc.yan@ossii.com.tw> 0.0.3-5
- update file: iqqi.conf

* Wed Aug 10 2011 Wind Win <yc.yan@ossii.com.tw> 0.0.3-4
- Bug fixed.

* Thu Aug  8 2011 Wind Win <yc.yan@ossii.com.tw> 0.0.3-3
- Bug fixed.

* Thu Aug  4 2011 Wind Win <yc.yan@ossii.com.tw> 0.0.3-2
- Bug fixed.

* Thu Jul 28 2011 Wind Win <yc.yan@ossii.com.tw> 0.0.3-1
- Added for some features: idiom...etc.

* Wed Jul 20 2011 Wind Win <yc.yan@ossii.com.tw> 0.0.2-5
- Added for some features.

* Fri Jul 15 2011 Wind Win <yc.yan@ossii.com.tw> 0.0.2-4
- Added for some features.

* Thu Jul 14 2011 Wind Win <yc.yan@ossii.com.tw> 0.0.2-3
- Added for some features.

* Tue Jul 12 2011 Wind Win <yc.yan@ossii.com.tw> 0.0.2-2
- Added for some features.

* Mon Jul 11 2011 Wind Win <yc.yan@ossii.com.tw> 0.0.2-1
- Some features added.

* Wed Jul 6 2011 Wind Win <yc.yan@ossii.com.tw> 0.0.1-1
- Build for first time.
