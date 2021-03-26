%define	fontdir	%{_datadir}/fonts/wang

Summary: H.T.Wang Free Fonts
Name: wang-fonts
Version: 1.3.0
Release: 5.1
License: GPLv2
Group: User Interface/X
BuildArch: noarch
#Source0: http://wangfonts.googlecode.com/files/wangfonts-%{version}.tar.gz
Source0: %{name}-%{version}.txz
URL: http://code.google.com/p/wangfonts/
Requires(post): fontconfig

%description
Free Chinese TrueType fonts 2004 donated by Prof. Hann-Tzong WANG.

%package extra
Summary: H.T.Wang Free Fonts Extra
Requires: %{name}

%description extra
Free Chinese TrueType fonts 2004 donated by Prof. Hann-Tzong WANG. (Extra)

%prep
%setup -q -n %{name}

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{fontdir}
install -m644 *.ttf %{buildroot}%{fontdir}

%clean
rm -rf %{buildroot}

%post
/usr/bin/fc-cache 2> /dev/null

%postun
/usr/bin/fc-cache 2> /dev/null

%files
%dir %{fontdir}
%{fontdir}/wt0*.ttf

%files extra
%{fontdir}/wt[a-z]*.ttf

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.0
- Rebuild for Fedora
