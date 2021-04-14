Name: mingliao-font
Summary: An elegant classic chinese sans font
Version: 1.0
Release: 3.1
License: Other
Group: System/X11/Fonts
#Source0: https://www.sugarsync.com/pf/D910303_67_8650538496?directDownload=true
Source0: mingliao_dev.ttf
BuildRoot: %{_tmppath}/build-root-%{name}
BuildArch: noarch
URL: http://www.byvoid.com/blog/mingliao-ofy

%description
An old-shaped chinese glyph font based on the japanese font Meiryo.

%prep
%setup -T -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/fonts
cp %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/fonts

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%{_datadir}/fonts/*.ttf

%changelog
* Sun Apr 28 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
