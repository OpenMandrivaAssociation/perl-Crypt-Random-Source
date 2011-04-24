%define upstream_name    Crypt-Random-Source
%define upstream_version 0.07

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    Base class for random devices
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Any::Moose)
BuildRequires: perl(Capture::Tiny)
BuildRequires: perl(Carp)
BuildRequires: perl(Errno)
BuildRequires: perl(File::Spec)
BuildRequires: perl(IO::File)
BuildRequires: perl(IO::Handle)
BuildRequires: perl(IO::Select)
BuildRequires: perl(Module::Find)
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(bytes)
BuildRequires: perl(namespace::clean)
BuildRequires: perl(ok)
Requires: perl(Module::Find)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides implementations for a number of byte oriented sources
of random data.

See the Crypt::Random::Source::Factory manpage for a more powerful way to
locate sources, and the various sources for specific implementations.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes LICENSE META.yml META.json
%{_mandir}/man3/*
%perl_vendorlib/*


