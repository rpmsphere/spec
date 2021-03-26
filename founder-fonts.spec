%define	fontdir	%{_datadir}/fonts/founder

Summary: FZ chinese Fonts
Name: founder-fonts
Version: 1.0
Release: 1%{?dist}
License: Unknown
Group: User Interface/X
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Source0: founder.zip
URL: http://www.foundertype.com/
Requires(post): fontconfig

%description
Founder is the largest developer of Chinese fonts. More than 90% of Chinese
newspapers and publishers worldwide use Founder fonts. Founder offers high
quality Chinese, Japanese and Korean (CJK) TrueType, Postscript, ATM and
Bitmap fonts for Windows, Macintosh, Unix and Linux platforms. With full
support for Unicode, our CJK fonts can be used on a variety of devices, from
computers to video equipment. In addition to the wide range of fonts readily
available for purchase, we can develop customized solutions to meet client's
special requirements.

%prep
%setup -q -c

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
%defattr(-, root, root)
%{fontdir}

%changelog
* Wed Feb 29 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- initial package
