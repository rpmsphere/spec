Name:           meego-bookmarks
Version:        2
Release:        1.1
Summary:        MeeGo bookmarks
Group:          Applications/Internet
License:        GFDL
URL:            http://meego.com/
Source0:        default-bookmarks.html
BuildArch:      noarch
Provides:       system-bookmarks


%description
This package contains the default bookmarks for MeeGo.

%prep
# We are nihilists, Lebowski.  We believe in nassing.

%build
# We are nihilists, Lebowski.  We believe in nassing.

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/bookmarks
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/bookmarks


%clean
%{__rm} -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%dir %{_datadir}/bookmarks
%{_datadir}/bookmarks/default-bookmarks.html

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuilt for Fedora
* Tue Oct 26 2010 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII
* Thu Jun 10 2010 awafaa@opensuse.org
- Initial import for openSUSE version 2
