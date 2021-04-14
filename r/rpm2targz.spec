Name:           rpm2targz
Version:        9.0.0.4g
Release:        5.1
License:        Any permissive
Summary:        Convert rpm File to Compressed tar Archive
URL:            http://www.slackware.com/config/packages.php
Group:          Productivity/Archiving/Compression
Source0:        http://gentoo.osuosl.org/distfiles/%{name}-%{version}.tar.lzma
Source1:        rpm2targz.1
Source2:        rpmunpack.1
# PATCH-FIX-UPSTREAM rpm2targz-lzma.patch http://bugs.gentoo.org/show_bug.cgi?id=321439 -- unpack lzma compressed rpms
Patch0:         rpm2targz-9.0.0.4g-lzma.patch
BuildRequires:  xz
Requires:       xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A simple utility to convert RPM packages into tar.gz, tar.bz2, tar.lzma,
tar.xz archives.

%prep
%setup -q
%patch0

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
install -dm 0755 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 0644 -t $RPM_BUILD_ROOT%{_mandir}/man1 %{SOURCE1} %{SOURCE2}
cd $RPM_BUILD_ROOT%{_mandir}/man1
for t in tar tarbz2 tbz2 tarlzma tgz tarxz txz ; do
    ln -sf rpm2targz.1 rpm2${t}.1
done

%files
%defattr(-,root,root,-)
%doc rpm2targz.README
%{_bindir}/rpm*
%doc %{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Aug 05 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 9.0.0.4g
- Rebuilt for Fedora
* Thu Nov 10 2011 lazy.kent@opensuse.org
- Added man pages.
- Changed URL.
- Use full URL as a source.
- spec clean up.
* Mon Apr 18 2011 lazy.kent@opensuse.org
- Patch to unpack lzma compressed rpms.
* Wed Dec 16 2009 lazy.kent.suse@gmail.com
- Initial package created - 9.0.0.4g.
