%define upstream_name    Crypt-Random-Source
Name:		perl-%{upstream_name}
Version:	0.14
Release:	2

Summary:	Base class for random devices
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/karenetheridge/Crypt-Random-Source
Source0:	https://cpan.metacpan.org/authors/id/E/ET/ETHER/Crypt-Random-Source-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Any::Moose)
BuildRequires:	perl(Capture::Tiny)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Errno)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(IO::Select)
BuildRequires:	perl(Module::Find)
BuildRequires:	perl(Module::Implementation)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(namespace::clean)
BuildRequires:	perl(ok)
Requires:	perl(Module::Find)
Requires:	perl(namespace::clean)
BuildArch:	noarch

%description
This module provides implementations for a number of byte oriented sources
of random data.

See the Crypt::Random::Source::Factory manpage for a more powerful way to
locate sources, and the various sources for specific implementations.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes LICENSE META.yml META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*
