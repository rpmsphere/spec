%define	fontdir	%{_datadir}/fonts/yozfont

Summary: Hand-writing freeware unicode fonts
Name: yozfont-fonts
Version: 14.04
Release: 2.1
License: SIL Open Font License
Group: User Interface/X
BuildArch: noarch
Source0: http://yozvox.web.fc2.com/YOz.7z
URL: http://yozvox.web.fc2.com/
Requires(post): fontconfig
BuildRequires: util-linux, p7zip

%description
Y.OzFont(s) is hand-writing sans-serif type of freeware unicode fonts.
Developed by Y.OzVox.

Pen-Ji Pack -- It seems to have written this with a water ballpoint.

%package common
Summary: Hand-writing freeware unicode fonts (common)

%description common
Y.OzFont(s) is hand-writing sans-serif type of freeware unicode fonts.
Developed by Y.OzVox.

Pen-Ji Pack -- It seems to have written this with a water ballpoint.
Common files for Y.OzFont

%package antique
Summary: Hand-writing freeware unicode fonts (antique)
Requires: %{name}-common

%description antique
Y.OzFont(s) is hand-writing sans-serif type of freeware unicode fonts.
Developed by Y.OzVox.

Pen-Ji Pack -- It seems to have written this with a water ballpoint.
Y.OzFont with antique kana.

%package cute
Summary: Hand-writing freeware unicode fonts (cute)
Requires: %{name}-common

%description cute
Y.OzFont(s) is hand-writing sans-serif type of freeware unicode fonts.
Developed by Y.OzVox.

Pen-Ji Pack -- It seems to have written this with a water ballpoint.
Y.OzFont with cute kana.

%package educational
Summary: Hand-writing freeware unicode fonts (educational)
Requires: %{name}-common

%description educational
Y.OzFont(s) is hand-writing sans-serif type of freeware unicode fonts.
Developed by Y.OzVox.

Pen-Ji Pack -- It seems to have written this with a water ballpoint.
Y.OzFont with educational kana.

%package new
Summary: Hand-writing freeware unicode fonts (new)
Requires: %{name}-common

%description new
Y.OzFont(s) is hand-writing sans-serif type of freeware unicode fonts.
Developed by Y.OzVox.

Pen-Ji Pack -- It seems to have written this with a water ballpoint.
Y.OzFont with new kana.

%package standard
Summary: Hand-writing freeware unicode fonts (standard)
Requires: %{name}-common

%description standard
Y.OzFont(s) is hand-writing sans-serif type of freeware unicode fonts.
Developed by Y.OzVox.

Pen-Ji Pack -- It seems to have written this with a water ballpoint.
Y.OzFont with standard kana.

%prep
%setup -q -n YOz

%build
rm *90*.ttf

%install
install -d %{buildroot}%{fontdir}
install -m 0644 *.ttf %{buildroot}%{fontdir}

%post
/usr/bin/fc-cache 2> /dev/null

%postun
/usr/bin/fc-cache 2> /dev/null

%files common
%doc *.txt
%dir %{fontdir}

%files antique
%{fontdir}/YOz?A*.ttf

%files cute
%{fontdir}/YOz?C*.ttf

%files educational
%{fontdir}/YOz?E*.ttf

%files new
%{fontdir}/YOz?N*.ttf

%files standard
%{fontdir}/YOz?S*.ttf

%changelog
* Thu Aug 18 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 14.04
- Rebuild for Fedora
