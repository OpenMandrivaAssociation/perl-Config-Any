%define upstream_name	 Config-Any
%define upstream_version 0.22

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Load configuration from different file formats, transparently
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Module::Pluggable) >= 3.01
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Config::General)
BuildRequires:	perl(Config::Tiny)
BuildRequires:	perl(JSON)
BuildRequires:	perl(YAML)
BuildRequires:	perl(XML::Simple)
BuildRequires:	perl(version)

BuildArch:	    noarch

%description
Config::Any provides a facility for Perl applications and libraries to
load configuration data from multiple different file formats. It
supports XML, YAML, JSON, Apache-style configuration, Windows INI
files, and even Perl code.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/Config


%changelog
* Tue Jul 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.220.0-1mdv2011.0
+ Revision: 688737
- update to new version 0.22

* Tue May 31 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.210.0-1
+ Revision: 682113
- update to new version 0.21

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.200.0-2
+ Revision: 680837
- mass rebuild

* Sun Aug 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.200.0-1mdv2011.0
+ Revision: 569931
- update to 0.20

* Tue Feb 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.190.0-1mdv2011.0
+ Revision: 506743
- update to 0.19

* Tue Nov 17 2009 Jérôme Quelin <jquelin@mandriva.org> 0.180.0-1mdv2010.1
+ Revision: 466748
- update to 0.18

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.170.0-1mdv2010.0
+ Revision: 406318
- rebuild using %%perl_convert_version

* Fri Feb 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.17-1mdv2009.1
+ Revision: 338063
- update to new version 0.17

* Sat Nov 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.16-1mdv2009.1
+ Revision: 305705
- update to new version 0.16

* Thu Nov 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.15-1mdv2009.1
+ Revision: 302891
- update to new version 0.15

* Sun Aug 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-1mdv2009.0
+ Revision: 270346
- update to new version 0.14

* Wed Apr 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-1mdv2009.0
+ Revision: 194922
- update to new version 0.12

* Tue Jan 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-1mdv2008.1
+ Revision: 159933
- update to new version 0.11

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Dec 13 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2008.1
+ Revision: 119232
- update to new version 0.10

* Wed Aug 29 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2008.0
+ Revision: 74278
- new version


* Fri Mar 09 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdv2007.1
+ Revision: 138795
- new version

* Mon Aug 28 2006 Scott Karns <scottk@mandriva.org> 0.04-2mdv2007.0
+ Revision: 58222
- Added BuildRequires perl(Test::Exception)

* Sat Aug 26 2006 Scott Karns <scottk@mandriva.org> 0.04-1mdv2007.0
+ Revision: 58057
- Import perl-Config-Any

* Sat Aug 26 2006 Scott Karns <scottk@mandriva.org> 0.04-1mdv2007.0
- Initial Mandriva RPM

