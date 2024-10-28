%define upstream_name    MP3-Tag
%define upstream_version 1.13

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Normalize::Text::Normalize_Fields\\)|perl\\(Music_Normalize_Fields\\)'
%else
%define _requires_exceptions perl(\\(Normalize::Text::Normalize_Fields\\|Music_Normalize_Fields\\))
%endif

Name:           perl-%{upstream_name}
Version:        %{upstream_version}
Release:        6.1
Summary:        Module for reading tags of MP3 audio files 
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            https://search.cpan.org/dist/%{upstream_name}
Source0:        https://www.cpan.org/modules/by-module/MP3/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:  perl-devel
BuildRequires:  perl(Compress::Zlib)
BuildArch:      noarch
Requires:       perl(Compress::Zlib)

%description
Tag is a wrapper module to read different tags of mp3 files. It provides an
easy way to access the functions of separate modules which do the handling
of reading/writing the tags itself.

At the moment MP3::Tag::ID3v1 and MP3::Tag::ID3v2 are supported for read and
write; MP3::Tag::Inf, MP3::Tag::CDDB_File, MP3::Tag::File,
MP3::Tag::LastResort are supported for read access (the information obtained
by parsing CDDB files, .inf file and the filename).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
# requires CDDB connection
rm -f t/mp3tag.t
chmod -R u+w examples
chmod 755 examples/*.pl examples/mp3info2 examples/typeset_audio_dir

%build
# -n is here to avoid installation of scripts (they come in examples/ anyway)
perl Makefile.PL INSTALLDIRS=vendor -n
make

%install
%make_install

%files
%doc Changes README.txt TODO examples
%{perl_vendorlib}/MP3
%{perl_vendorlib}/Encode
%{perl_vendorlib}/Normalize
%{_mandir}/*/*
%exclude %{_libdir}/perl5/perllocal.pod
%{_libdir}/perl5/vendor_perl/auto/MP3/Tag/.packlist

%changelog
* Mon Aug 27 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.13
- Rebuilt for Fedora
* Fri Feb 17 2017 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1.130.0-6
- (530ea56) MassBuild#1257: Increase release tag
