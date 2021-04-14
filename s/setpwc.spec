Name:               setpwc
Version:            1.3
Release:            3.1
Summary:            Control all settings on Philips WebCams
Source:             http://www.vanheusden.com/setpwc/setpwc-%{version}.tgz
Patch1:             setpwc-optflags.patch
URL:                http://www.vanheusden.com/setpwc/
Group:              Hardware/Other
License:            GNU General Public License version 2 or later (GPL v2 or later)
BuildRoot:          %{_tmppath}/build-%{name}-%{version}
BuildRequires:      gcc make glibc-devel
BuildRequires:      kernel-headers >= 2.6.32

%description
setpwc allows users to set all settings of a Philips (or compatible) WebCam,
including auto-gain-control, color-balance, etc. Settings can be stored to the
non- volatile RAM of the Webcam and a dump of the current settings can be
retrieved.

%prep
%setup -q
%patch1

%build
%__make %{?_smp_flags} \
    CC="%__cc" \
    OPTFLAGS="%{optflags}"

%install
%__rm -rf "$RPM_BUILD_ROOT"
%__install -D -m0755 setpwc "$RPM_BUILD_ROOT%{_bindir}/setpwc"
%__install -D -m0644 setpwc.1 "$RPM_BUILD_ROOT%{_mandir}/man1/setpwc.1"

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc license.txt readme.txt
%{_bindir}/setpwc
%doc %{_mandir}/man1/setpwc.1.*

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3
- Rebuilt for Fedora

* Sun May 22 2011 pascal.bleser@opensuse.org
- initial version (1.3)
