Summary: Interactive study screen
Name: oxstudy
Version: 0.1
Release: 2
License: Commercial
Group: Applications/Multimedia
Source0: %{name}.tar.gz
Requires: oxzilla
BuildArch: noarch

%description
Interactive study screen using OXZilla.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT

%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/
cd $RPM_BUILD_ROOT%{_datadir}/
tar zxf %{SOURCE0}
cd -

mkdir -p $RPM_BUILD_ROOT%{_bindir}
%__cat >$RPM_BUILD_ROOT%{_bindir}/oxstudy <<EOF
#!/bin/bash
cd %{_datadir}/oxstudy
oxzilla -s 440x705 oxstudy.htm
EOF

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0777,root,root,0777)
%{_datadir}/oxstudy
%{_bindir}/oxstudy

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuilt for Fedora
* Mon Apr 19 2010 Kami <kami@ossii.com.tw> 0.1-2
- Building on first time.

* Fri Mar 19 2010 Kami <kami@ossii.com.tw> 0.1-1
- Building on first time.
