Summary:	A minimalist web browser
Name:		xxxterm
Version:	1.11.3
Release:	12.1
License:	MIT
Group:		Networking/WWW
URL:		https://opensource.conformal.com/wiki/XXXTerm
Source0:	https://opensource.conformal.com/snapshots/xxxterm/%{name}-%{version}.tgz
Patch0:		xxxterm-1.8.0-mdv-desktop.patch
Patch1:		xxxterm-1.11.3-link-javascriptcoregtk.patch
Patch2:		0001-Change-default-homepage.patch
# From Debian unchanged
Patch10:	0002-Fix-resources-dir.patch
Patch11:	0006-Add-missing-includes.patch
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libbsd)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(webkit-1.0)
BuildRequires:	libgcrypt-devel

%description
xxxterm is a minimalist web browser with sophisticated security features
designed-in (rather than through an add-on). In particular, it provides both
persistent and per-session controls for scripts and cookies, making it easy
to thwart tracking and scripting attacks.

In additional to providing a familiar mouse-based interface like other web
browsers, it offers a set of vi-like keyboard commands for users who prefer
to keep their hands on their keyboard.

The default settings provide a secure environment. With simple keyboard
commands, the user can "whitelist" specific sites, allowing cookies and
scripts from those sites.

%files
%doc %{_docdir}/%{name}/LICENSE
%{_mandir}/man1/xxxterm.*
%{_bindir}/xxxterm
%{_datadir}/applications/xxxterm.desktop
%{_datadir}/xxxterm/style.css
%{_datadir}/xxxterm/xxxterm*.png
%{_datadir}/xxxterm/tld-rules
%{_datadir}/icons/hicolor/*/apps/xxxterm.png

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch10 -p1
%patch11 -p1

%build
export CFLAGS="%{optflags}"
cd linux
%make_build \
	OPTIMIZE="%{optflags}" \
	PREFIX=%{_prefix}

%install
pushd linux
make install PREFIX=%{buildroot}%{_prefix}
popd
for s in 16 32 48 64 128; do
	install -d -m 0755 %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/
	ln -s ../../../../xxxterm/xxxtermicon${s}.png %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/xxxterm.png
done
install -D -m 0644 xxxterm.desktop %{buildroot}%{_datadir}/applications/xxxterm.desktop
install -D -m 0644 style.css %{buildroot}%{_datadir}/xxxterm/style.css
install -d -m 0755 %{buildroot}/%{_docdir}/xxxterm
cat > %{buildroot}/%{_docdir}/%{name}/LICENSE << EOF
-= License =-

/*
 * Copyright (c) 2010, 2011 Marco Peereboom <marco@peereboom.us>
 * Copyright (c) 2011 Stevan Andjelkovic <stevan@student.chalmers.se>
 * Copyright (c) 2010, 2011 Edd Barrett <vext01@gmail.com>
 * Copyright (c) 2011 Todd T. Fries <todd@fries.net>
 * Copyright (c) 2011 Raphael Graf <r@undefined.ch>
 * Copyright (c) 2011 Michal Mazurek <akfaew@jasminek.net>
 *
 * Permission to use, copy, modify, and distribute this software for any
 * purpose with or without fee is hereby granted, provided that the above
 * copyright notice and this permission notice appear in all copies.
 *
 * THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
 * WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
 * ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
 * WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
 * ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
 * OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
 */

-= javascript.h license =-

Javascript code was borrowed from the friendly folks at vimprobable2 under the following license:

/*
Copyright (c) 2009 Leon Winter
Copyright (c) 2009-2011 Hannes Schueller
Copyright (c) 2009-2010 Matto Fransen
Copyright (c) 2010-2011 Hans-Peter Deifel
Copyright (c) 2010-2011 Thomas Adam
Copyright (c) 2011 Albert Kim
Copyright (c) 2011 Daniel Carl

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
*/
EOF

%changelog
* Fri Jun 22 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.11.3
- Rebuild for Fedora
* Fri Feb 17 2017 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1.11.3-5
- (5f7758f) MassBuild#1257: Increase release tag
