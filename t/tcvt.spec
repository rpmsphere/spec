Name: tcvt
Summary: Multicolumn Virtual Terminal
Version: 0.1.20170117
License: 2-clause BSD
Release: 1.1
Group: utils
URL: http://subdivi.de/~helmut/tcvt/
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

%description
Your screen is getting wider. Keeping track of long lines gets harder. Space
on the right hand side of the screen is completely blank due to short lines.
Are you struggling with these? Then tcvt is for you.

The two column virtual terminal, short tcvt, can be used to vertically split a
single terminal in two (or more) columns. This is similar to a two column
layout in printing, just for regular terminals.

Note that this is not about placing two terminals next to each other. This
task is already solved by tiling window managers, screen, tmux and splitvt.
What tcvt does is create a single very tall terminal with two columns.

Please note that the current version does not support UTF-8 yet. Experimental
patches are available in the utf8 branch of the upstream repository.

%prep
%setup -q -n %{name}

%build

%install
make install PREFIX=/usr DESTDIR=%{buildroot}

%files
%doc README.md
%{_bindir}/*%{name}
%{_mandir}/man1/*%{name}.1.*

%changelog
* Fri Nov 03 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.20170117
- Rebuild for Fedora
